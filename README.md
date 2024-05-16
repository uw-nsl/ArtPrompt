<h1 align='center' style="text-align:center; font-weight:bold; font-size:2.0em;letter-spacing:2.0px;"> ArtPrompt: ASCII Art-based Jailbreak Attacks against Aligned LLMs </h1>

<p align='center' style="text-align:center;font-size:1.25em;">
    <a href="https://scholar.google.com/citations?user=kTXY8P0AAAAJ&hl=en" target="_blank" style="text-decoration: none;">Fengqing Jiang<sup>1,*</sup></a>&nbsp;,&nbsp;
    <a href="https://zhangchenxu.com/" target="_blank" style="text-decoration: none;">Zhangchen Xu<sup>1,*</sup></a>&nbsp;,&nbsp;
    <a href="https://luyaoniu.github.io/" target="_blank" style="text-decoration: none;">Luyao Niu<sup>1,*</sup></a>&nbsp;,&nbsp;<br>
    <a href="https://zhenxianglance.github.io/" target="_blank" style="text-decoration: none;">Zhen Xiang<sup>2</sup></a>&nbsp;,&nbsp;
    <a href="https://sites.google.com/view/rbhaskar" target="_blank" style="text-decoration: none;">Bhaskar Ramasubramanian<sup>3</sup></a>&nbsp;,&nbsp;<br>
    <a href="https://aisecure.github.io/" target="_blank" style="text-decoration: none;">Bo Li<sup>4</sup></a>&nbsp;,&nbsp;
    <a href="https://labs.ece.uw.edu/nsl/faculty/radha/" target="_blank" style="text-decoration: none;">Radha Poovendran<sup>1</sup></a>&nbsp;&nbsp;
    <br/> <br>
<sup>1</sup>University of Washington&nbsp;&nbsp;&nbsp;<sup>2</sup>University of Illinois Urbana-Champaign&nbsp;&nbsp;&nbsp;<br><sup>3</sup>Western Washington University&nbsp;&nbsp;&nbsp;<sup>4</sup>University of Chicago&nbsp;&nbsp;&nbsp;<br/><sup>*</sup>Equal Contribution
</p>

<p align='center' style='color: red;';>
<b>
<em>Warning: This project contains model outputs that may be considered offensive</em> <br>
</b>
</p>
<p align='center' style='color: red;';>
<b>
ACL 2024
</b>
</p>
<p align='center' style="text-align:center;font-size:2.5 em;">
<b>
    <a href="https://arxiv.org/abs/2402.11753" target="_blank" style="text-decoration: none;">[arXiv]</a>
</b>
</p>

## Overview
![](asset/artprompt.jpg) 


## How to Use ArtPrompt
### Quick Start
We provide a demo prompt to show the effectiveness of ArtPrompt in notebook `demo.ipynb` (also at `demo_prompt.txt`). This is a successful prompt toward `gpt-4-0613`.

### Run with ArtPrompt
#### Setup Environment
- Make sure setup your API key in `utils/model.py` (or in environment) before running experiment.

#### Running
Run evaluation on `vitc-s` dataset. More details please refer to `benchmark.py`
```python
# at dir ArtPrompt
python benchmark.py --model gpt-4-0613 --task s
```

Run jailbreak with ArtPrompt. More details please refer to `baseline.py`
```python
cd jailbreak
python baseline.py --model gpt-4-0613 --tmodel gpt-3.5-turbo-0613 
```

You could use `--mp` arg to accelerate the inference time based on the available cpu cores on your machine.

## Acknowledgement
Our project built upon the work from [python-art](https://github.com/sepandhaghighi/art),[llm-attack](https://github.com/llm-attacks/llm-attacks), [AutoDan](https://github.com/SheltonLiu-N/AutoDAN), [PAIR](https://github.com/patrickrchao/JailbreakingLLMs), [DeepInception](https://github.com/tmlr-group/DeepInception), [LLM-Finetuning-Safety](https://github.com/LLM-Tuning-Safety/LLMs-Finetuning-Safety), [BPE-Dropout](https://github.com/VProv/BPE-Dropout). We appreciated these open-sourced work in the community.


## Citation
If you find our project useful in your research, please consider citing:

```
@misc{jiang2024artprompt,
      title={ArtPrompt: ASCII Art-based Jailbreak Attacks against Aligned LLMs}, 
      author={Fengqing Jiang and Zhangchen Xu and Luyao Niu and Zhen Xiang and Bhaskar Ramasubramanian and Bo Li and Radha Poovendran},
      year={2024},
      eprint={2402.11753},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```





