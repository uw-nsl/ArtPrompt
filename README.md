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
    <a href="https://aclanthology.org/2024.acl-long.809/" target="_blank" style="text-decoration: none;">[Paper]</a>
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

- You could use `--mp` arg to accelerate the inference time based on the available cpu cores on your machine.

- `--ps` flag is used to set the font setup for our method. We have font name sets used for evaluation stated in our paper, please refer to Appendix A.3 for details. Specially, the top-1 setup in table 3 use `vitc-h-gen`, and ensemble use `vitc-h-gen/alphabet/keyboard/cards/letters/puzzle`,  please run each font to generate the individual result and use the `ensemble_eval.ipynb` notebook for ensemble evaluation results. The top-1 setup is subject to change given the different setups of victim models, we determined the top-1 font based on the average performance on our victim model sets.

## Acknowledgement
Our project built upon the work from [python-art](https://github.com/sepandhaghighi/art),[llm-attack](https://github.com/llm-attacks/llm-attacks), [AutoDan](https://github.com/SheltonLiu-N/AutoDAN), [PAIR](https://github.com/patrickrchao/JailbreakingLLMs), [DeepInception](https://github.com/tmlr-group/DeepInception), [LLM-Finetuning-Safety](https://github.com/LLM-Tuning-Safety/LLMs-Finetuning-Safety), [BPE-Dropout](https://github.com/VProv/BPE-Dropout). We appreciated these open-sourced work in the community.


## Citation
If you find our project useful in your research, please consider citing:

```
@inproceedings{jiang-etal-2024-artprompt,
    title = "{A}rt{P}rompt: {ASCII} Art-based Jailbreak Attacks against Aligned {LLM}s",
    author = "Jiang, Fengqing  and
      Xu, Zhangchen  and
      Niu, Luyao  and
      Xiang, Zhen  and
      Ramasubramanian, Bhaskar  and
      Li, Bo  and
      Poovendran, Radha",
    editor = "Ku, Lun-Wei  and
      Martins, Andre  and
      Srikumar, Vivek",
    booktitle = "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.acl-long.809",
    doi = "10.18653/v1/2024.acl-long.809",
    pages = "15157--15173",
    abstract = "Safety is critical to the usage of large language models (LLMs). Multiple techniques such as data filtering and supervised fine-tuning have been developed to strengthen LLM safety. However, currently known techniques presume that corpora used for safety alignment of LLMs are solely interpreted by semantics. This assumption, however, does not hold in real-world applications, which leads to severe vulnerabilities in LLMs. For example, users of forums often use ASCII art, a form of text-based art, to convey image information. In this paper, we propose a novel ASCII art-based jailbreak attack and introduce a comprehensive benchmark Vision-in-Text Challenge (ViTC) to evaluate the capabilities of LLMs in recognizing prompts that cannot be solely interpreted by semantics. We show that five SOTA LLMs (GPT-3.5, GPT-4, Gemini, Claude, and Llama2) struggle to recognize prompts provided in the form of ASCII art. Based on this observation, we develop the jailbreak attack ArtPrompt, which leverages the poor performance of LLMs in recognizing ASCII art to bypass safety measures and elicit undesired behaviors from LLMs. ArtPrompt only requires black-box access to the victim LLMs, making it a practical attack. We evaluate ArtPrompt on five SOTA LLMs, and show that ArtPrompt can effectively and efficiently induce undesired behaviors from all five LLMs.",
}
```





