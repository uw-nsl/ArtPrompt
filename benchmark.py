import argparse
from tqdm.auto import tqdm
import json

from utils.model import load_model, genai, gemini_apis
from utils.dataset import load_dataset, data_aug
from utils.prompt import task_prompt
from utils.eval import eval_res




def path_parser(save_dir, args):
    path = f"{save_dir}/{args.model}_vitc-{args.task}_t{args.t}_ps-{args.ps}"
    if args.aug:
        path += "_aug"

    if args.ft is not None:
        path += f"_ft{args.ft}"

    if args.num != -1:
        path += f"_num{args.num}"
    else:
        path += "_all"

    return path + ".json"

def inference_mp(args):
    model_name, api_idx,  idx, atext, label, ps, aug, debug = args
    if model_name == 'gemini':
        api_idx = idx % 2
    model = load_model(model_name, api_idx)
    ascii_repr = atext
    ascii_repr = data_aug(ascii_repr, aug)
    label = label
    prompt = task_prompt(ps, ascii_repr, label, model_name)
    response = model(prompt, n=1, debug=debug)
    return idx, model.resp_parse(response)

def main(args):
    model = load_model(args.model, args.api)
    args.t = model.T
    dataset = load_dataset(args.task, args.ft)
    print("Start running inference")
    # run inference
    res = []
    if args.num != -1:
        dataset = dataset[:args.num]

    
    file_path = path_parser("result", args)
    if not args.eval_only:
        if args.mp > 1: # use multiprocessing
            print("Using multiprocessing")
            # genai.configure(api_key=gemini_apis[args.api])
            from multiprocessing import Pool
            if args.model != 'gemini':
                mp_arg_list = [(args.model, args.api, i, data['art_text'], data['text'], args.ps, args.aug, args.debug) for i, data in enumerate(dataset)]
            else:
                print('use gemini api pool')
                mp_arg_list = [(args.model, i%len(gemini_apis), i, data['art_text'], data['text'], args.ps, args.aug, args.debug) for i, data in enumerate(dataset)]        
            
            with Pool(args.mp) as p:
                res = list(tqdm(p.imap(inference_mp, mp_arg_list), total=len(dataset)))

            res = sorted(res, key=lambda x: x[0])
            res = [r[1] for r in res]
        else:
            for i in tqdm(range(len(dataset))):
                data = dataset[i]
                ascii_repr = data['art_text']
                ascii_repr = data_aug(ascii_repr, args.aug)
                label = data['text']
                prompt = task_prompt(args.ps, ascii_repr, label, args.model)
                response = model(prompt, n=1, debug=args.debug)

                res.append(model.resp_parse(response))

        # save result
        with open(file_path, "w") as f:
            json.dump(res, f, indent=4)

    # eval
    print("Start running evaluation")
    res = json.load(open(file_path, "r"))
    if args.task == 's' or args.task == 'mnist':
        correct = 0
        for i in range(len(res)):
            if eval_res(res[i][0], dataset[i]['text']):
                correct += 1

        print(f"Accuracy: {correct/len(res)}")

    elif args.task == 'l':
        # evaluate Acc and AMR
        correct = 0
        AMR = 0
        for i in range(len(res)):
            correct_i, AMR_i = eval_res(res[i][0], dataset[i]['text'], AMR=True)
            if correct_i:
                correct += 1
            AMR += AMR_i


        print(f"Accuracy: {correct/len(res)}")
        print(f"AMR: {AMR/len(res)}")
    else:
        raise ValueError(f"task should be s or l, but got {args.task}")
    

    return    


        



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--model", type=str, default="gpt-4-0613", help="Model name for evaluation")
    args.add_argument("--task", type=str, default="s", help="s or l")
    args.add_argument("--num", type=int, default=-1, help="Number of samples to run inference")
    args.add_argument("--t", type=float, default=0, help="Temperature for inference")
    args.add_argument("--ps", type=str, default="zs-s-easy", help="Prompt setting for inference")
    args.add_argument("--mp", type=int, default=1, help="multi-processing for inference")
    args.add_argument("--api", type=int, default=0, help="index for api pool")
    args.add_argument("-aug", action="store_true", help="Whether to use data augmentation")

    args.add_argument("-eval_only", action="store_true", help="Only run evaluation")
    args.add_argument("-debug", action="store_true", help="Run in debug mode")
    

    args = args.parse_args()
    print(args)
    main(args)