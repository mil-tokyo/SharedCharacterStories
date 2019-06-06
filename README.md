# Shared-Character Stories

This directory contains the Shared-Character Stories dataset and annotations for its subset. 
They are introduced in our paper:

Yusuke Mori, Hiroaki Yamane, Yoshitaka Ushiku, Tatsuya Harada, "How narratives move your mind: A corpus of shared-character stories for connecting emotional flow and interestingness," Information Processing & Management, 2019.
[Link](https://doi.org/10.1016/j.ipm.2019.03.006)

## Contents

### Collected Stories
- ./stories/condstories.csv
  - collected 759 stories
      - story id
      - two-character setting
      - sentence 1 ~ 5 of the story
  - Note that “athlete” was misspelled as “athelete” in our settings, but no workers seemed to be confused by the typo.
  

### Emotion Evaluation (Amazon MTurk)
- ./emotion_evaluation/small_task_allinfo.csv
  - 100 stories used for annotation (75 human-written, 25 artificial managed)
      - story id
      - two-character setting
      - sentence 1 ~ 5 of the story
      - two-character names
      - two-character setting with the names replaced
      - type : a condition of the story {human-written, random last sentence, random last sentence from the same setting, random order}
  
- ./emotion_evaluation/eval_results.csv
  - evaluated results (623 answers)
      - story id
      - sentence 1 ~ 5 of the story
      - Review
      - Valence and Arousal of each sentence from the points of view of Character 1, Character 2, and Reader 
      - Five Evaluation Aspects
          - clearness (clarity)
          - consistency
          - fluency	
          - meaning	
          - storyness	
      - rating : a total score
      - Title : a title of the story (for 25 artificial managed stories, the title of the original human-written stories are shown)
      - type : a condition of the story {human-written, random last sentence, random last sentence from the same setting, random order}

### Visualization
- ./emotion_evaluation/vis_eval_results.ipynb
  - using ./src/emotionplot.py


## Copyright
The content of this project itself is licensed under the [Creative Commons Attribution-ShareAlike 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/), and the underlying source code used to format and display that content is licensed under the [MIT license](LICENSE.md).


## Citation:
	@article{mori2019sharedcharacters,
        title = "How narratives move your mind: A corpus of shared-character stories for connecting emotional flow and interestingness",
        journal = "Information Processing & Management",
        year = "2019",
        issn = "0306-4573",
        doi = "https://doi.org/10.1016/j.ipm.2019.03.006",
        author = "Yusuke Mori and Hiroaki Yamane and Yoshitaka Ushiku and Tatsuya Harada",
    }