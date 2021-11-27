# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Standardized Test Analysis

### Background and Introduction
The SAT and ACT are standardized tests that many colleges and universities in the United States require for their admissions process. This score is used along with other materials such as grade point average (GPA) and essay responses to determine whether or not a potential student will be accepted to the university.

The SAT has two sections of the test: Evidence-Based Reading and Writing and Math ([*source*](https://www.princetonreview.com/college/sat-sections)). The ACT has 4 sections: English, Mathematics, Reading, and Science, with an additional optional writing section ([*source*](https://www.act.org/content/act/en/products-and-services/the-act/scores/understanding-your-scores.html)). They have different score ranges, which you can read more about on their websites or additional outside sources (a quick Google search will help you understand the scores for each test):
* [SAT](https://collegereadiness.collegeboard.org/sat)
* [ACT](https://www.act.org/content/act/en.html)

Standardized tests have long been a controversial topic for students, administrators, and legislators. Since the 1940's, an increasing number of colleges have been using scores from sudents' performances on tests like the SAT and the ACT as a measure for college readiness and aptitude ([*source*](https://www.minotdailynews.com/news/local-news/2017/04/a-brief-history-of-the-sat-and-act/)). Supporters of these tests argue that these scores can be used as an objective measure to determine college admittance. Opponents of these tests claim that these tests are not accurate measures of students potential or ability and serve as an inequitable barrier to entry.

While many students continue to be unable to take the tests due to the impact of covid-19, some schools have chosen to extend their Test Optional Policy. However there is still a sizeable number of schools that require the testing despite the circumstances. Whether the Test Optional policy stays and for how many more years, we are uncertain but we foresee that the testing will be reinstated once situations stablise across the globe. 

In a bid to empower every students in all the states to measure up to the national mean as the immediate goal, the group will be looking into each state's overall performance and pick out the underperforming states before analysing deeper which and how exactly to help. 

Between the ACT and SAT tests, we identified the SAT scores to focus on because we see an upward trend in the take-up rate for SAT tests. Also further research has reinforced our choice of SAT as the better investigative dataset because the resigned SAT since 2016 has been mandated by many states as it prioritises content that prepare students for the reading and math skills needed for college and future work situations. Furthermore, the College Board has also accelerated its plans to digitalise the SAT test due to the situation that makes in-house testing a challenge to implement. In summary, the SAT will be here to stay so our group would like to be able to provide funding where necessary to level the playing field for all students so they each have the oppportunity to conquer the SAT which can in turn propel them further beyond.

### Problem Statement
As a philanthropy group in US focused on equal education, the group is actively allocating funds to allow every state to compare up to the national’s mean scoring in a standardized test.

As part of the team, we are tasked to analyze National SAT data and present our findings to a non-technical audience and provide recommendations on suitable funding strategy.


### Data Dictionary
|Feature|Type|Dataset|Description|
|---|---|---|---|
|state|object|sat_combined|The state for which the data applies to.| 
|sat17_readwrite|int|sat_combined|The average SAT score for the Reading and Writing component for the year 2017. | 
|sat17_math|int|sat_combined|The average SAT score for the Math component for the year 2017.| 
|sat17_total|int|sat_combined|The average SAT total score for the year 2017.| 
|sat17_partrate|float|sat_combined|The participation rate of students in the state who took the test for the year 2017.| 
|sat18_readwrite|int|sat_combined|The average SAT score for the Reading and Writing component for the year 2018. | 
|sat18_math|int|sat_combined|The average SAT score for the Math component for the year 2018.| 
|sat18_total|int|sat_combined|The average SAT total score for the year 2018.| 
|sat18_partrate|float|sat_combined|The participation rate of students in the state who took the test for the year 2018.|
|sat19_readwrite|int|sat_combined|The average SAT score for the Reading and Writing component for the year 2019. | 
|sat19_math|int|sat_combined|The average SAT score for the Math component for the year 2019.| 
|sat19_total|int|sat_combined|The average SAT total score for the year 2019.| 
|sat19_partrate|float|sat_combined|The participation rate of students in the state who took the test for the year 2019.|

|Feature|Type|Dataset|Description|
|---|---|---|---|
|state|object|act_combined|The state for which the data applies to.| 
|act17_eng|int|act_combined|The average ACT score for the English component for the year 2017. | 
|act17_math|int|act_combined|The average ACT score for the Math component for the year 2017.| 
|act17_read|int|act_combined|The average ACT score for the Reading component for the year 2017. | 
|act17_sci|int|act_combined|The average ACT score for the Science component for the year 2017.| 
|act17_comp|int|act_combined|The average ACT composite score for the year 2017.| 
|act17_partrate|float|act_combined|The participation rate of students in the state who took the test for the year 2017.| 
|act18_eng|int|act_combined|The average ACT score for the English component for the year 2018. | 
|act18_math|int|act_combined|The average ACT score for the Math component for the year 2018.| 
|act18_read|int|act_combined|The average ACT score for the Reading component for the year 2018. | 
|act18_sci|int|act_combined|The average ACT score for the Science component for the year 2018.| 
|act18_comp|int|act_combined|The average ACT composite score for the year 2018.| 
|act18_partrate|float|act_combined|The participation rate of students in the state who took the test for the year 2018.|
|act19_eng|int|act_combined|The average ACT score for the English component for the year 2019. | 
|act19_math|int|act_combined|The average ACT score for the Math component for the year 2019.| 
|act19_read|int|act_combined|The average ACT score for the Reading component for the year 2019. | 
|act19_sci|int|act_combined|The average ACT score for the Science component for the year 2019.| 
|act19_comp|int|act_combined|The average ACT composite score for the year 2019.| 
|act19_partrate|float|act_combined|The participation rate of students in the state who took the test for the year 2019.|

### EDA
The SAT mean scores for all the 3 components - Total, Reading & Writing and Math - are on a downward trend. 

| Score | 2017 |  2018 | 2019 |
| --- | --- | --- | --- |
| Total | 1126 | 1120 | 1113 |
| Readwrite | 569 | 564 | 561 |
| Math | 556 | 556 | 552 |

Initial correlations identified: 
1. Participation rate and test scores are negatively correlated. Hence there exists an investigative bias if we were to pick out underperforming states using the mean scores.

2. There is a clear positive correlation between the Reading & Writing scores and the Math scores. Generally when a state does well in 1 component, it typically does just as well in the other component.

Subsequently various visualizations helped to narrow our scope: 

3. The histograms did not yield much since the means for each year were not normally distributed.

4. The boxplot provided a sense that the country generally did better in the Reading and Writing component than the Math component. If subsequent plans in the future involve how to up states' overall standards, this can be useful in zooming in on what exactly to focus on. 

5. The scatterplot helped to seal the direct relationship between the Reading and Writing and Math components. It also enabled the picking out of the outliers though there weren't many.

6. Aside from the SAT scores, a boxplot for the ACT scores of the corresponding years also backed up that observation that all states generally do well in Reading. Quite surprisingly, the English component is the poorest performing component out of the 4, with Math being the second poor performing component. 

7. The subsequent scatterplots enabled us to confirm the few underperforming states picked out and how further information about their percentage of economically disadvantaged and students with disabilities coupled with deeper research online enabled us to finalise the states we will provide funding to.


### Conclusion and recommendation
As a whole, the country generally performed better in the Reading and Writing component with the Math component score consistently trailing behind for all 3 years. This can point towards a need to look into the country's Math curriculum, teaching methods and scoring systems among other things to possibly bring the standard of the subject up to par. 

As our group's main aim was to provide funding for states to help improve the test scoring, we will zoom in to these specific states: 

1. **District of Columbia** 
- Poorest performing state for all 3 years.
- Urgently require intervention.
- Researched online and found out that this state sees high school dropout rates yet is one of the states with [high](https://www.census.gov/newsroom/press-releases/2021/public-school-spending-per-pupil.html) public school spending per pupil. It also ranks low on economic disadvantage as well as students with disabilities. This gives us a rather positive picture of how the state is doing yet in terms of its education system the jarring observation is that they are performing very poorly academically. So from our group's perspective, intervention for this state will not be in the form of funding. The problem here seems more deeply rooted than it seems as its people generally do not have faith in their public education system, something that will have to be tackled through various hierarchical levels within the country to engage all stakeholders to come to an agreement on the subsequent steps to take to better the situation. 


2. **Delaware** 
- Ranked 2nd as underperforming state for all 3 years.
- Picked out from our visualizations that it is high on economic disadvantage as well as students with disabilities. 
- Online research showed that the state generally enjoys [reasonable](https://www.census.gov/newsroom/press-releases/2021/public-school-spending-per-pupil.html) public school spending per pupil. The state also reports low incidence of bullying hence the overall picture of the education system in Delaware is less problematic. 
- This gives our group a clear perspective that funding, particularly targeted to those in economically challenged backgrounds should be of help to turn the situation around for them. 

3. **Idaho**
- Ranked 3rd as underforming states for all 3 years.
- Provide intervention.
- Online research showed that this state's public school spending per pupil is [low](https://www.census.gov/newsroom/press-releases/2021/public-school-spending-per-pupil.html). 
- In our above visualizations, Idaho ranks average in students with disabilities but high on the economically disadvantaged. 
- This also gives our group a clearer indication that funding will help this state, be it directly to the education of the students or for students of more economically challenged background. 

4. **Alabama & Arkansas**
- Low participation rates and poor test scores for all 3 years.
- Both states rank high on percentage of economically disadvantaged as well as students with disabilities. 
- Online research shows that both states enjoy a [decent](https://www.census.gov/newsroom/press-releases/2021/public-school-spending-per-pupil.html) amount of public school spending per pupil.
- So funding in this case can be more targeted at those from economically challenged backgrounds. 


5. **Florida** 
- Math score for 2019 was below expectations.
- Ranks high on percentage of economically disadvantaged and students with disabilities. 
- Although not underperforming so much so that it is in need of urgent intervention, our group can still provide funding to this state because we see potential in their abilities from their Reading and Writing performances to do better for the Math component in order to develop all roundedness in their achievements.
- So funding in this case can involve a comprehensive look into their current teaching practices, what worked well for their Reading and Writing components, knowing more about their student profiles to think up engaging practices to adopt in their Math teaching. 

The top performing states identified can also help us in our group's aim. We can consider funding a program where selected school staff (of varying hierarchical levels) can be seconded to the schools in these top performing states to observe and pick out best practices they can bring back to their schools to implement. 

5. **Virginia** (Top performing state for Reading and Writing component for 2018 and 2019)


6. **Massachusetts** (Top performing state for Math component for 2018 and 2019) 



- Look into what the schools in this states typically do to teach the aspect they have proven outstanding in; differentiated resources, varied teaching methods, engagement of students etc
- Share good practices with schools in other states, or even encourage a system of secondment of teaching officers to go from state to state to implement their good practices
- Consider pushing the standard of the other component up to achieve a win-win scenario

It is however worth a mention, that the allocation of funding with the intention of pulling up the academic performance of the states, will have to take into account more than just test scores and the few other aspects we have explored here. Digging deeper into the family nucleus of the population, availability of affordable education, teacher-student ratio, number of public schools in each state as well as the education levels of the general population all play a part in how the students are performing in schools which in turn translate to how they perform for the SAT test. 



### References

1. Gained insightful understanding of the [demographics](https://web.archive.org/web/20200919005506/https://reports.collegeboard.org/sat-suite-program-results) of the test takers for each state. 
2. Verified the 2018 SAT test scores with this [website](https://ipsr.ku.edu/ksdata/ksah/education/6ed16.pdf) as we found some suspiciously identical scores for some states.
3. Needed the component scores for [2018](https://nces.ed.gov/programs/digest/d18/tables/dt18_226.60.asp) and [2019](https://nces.ed.gov/programs/digest/d19/tables/dt19_226.60.asp) ACT tests to study links, if any with the SAT performances. 
4. We explored this site: [Public School Spending Per Pupil](https://www.census.gov/newsroom/press-releases/2021/public-school-spending-per-pupil.html) to understand better how public school spending per pupil differed across states in order to analyse better the situation within specific states we have identified.
5. We also ventured into this site: [States with the Best and Worst school systems](https://wallethub.com/edu/e/states-with-the-best-schools/5335#expert=mark-fabrizi) to delve deeper into the schooling systems in specific states to back our analysis up.
6. We also looked at the [educational status](https://www.thrillist.com/news/nation/most-educated-states-in-us-mapped) of the states in the country to understand better their performance in the tests.
7. We also explored more information about the states [here](https://nces.ed.gov/programs/digest/d20/tables/dt20_219.46.asp), particularly about their economic status to be able to formulate clearer suggestions on how best to help the states identified.

