# Project 2 - Ames Housing Data and Kaggle Challenge

In this project, we have been tasked to create a regression model based on the Ames Housing Dataset to predict the price of a house on sale. The [Ames Housing Dataset](https://www.kaggle.com/c/dsi-us-11-project-2-regression-challenge) is a robust dataset with over 70 columns of different [features](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt) relating to houses so it is up to us to pick out the most significant features that contribute to the selling price of the house. 


### The Data Science Process

**Problem Statement**

Property flipping is an investment strategy. All investments have risks.

To help novice property flippers manage risks, we will provide consultation upon application, based on our home valuation application that predicts the sale prices of homes in Ames, Iowa. We have modeled Linear Regression, Ridge, Lasso and Grid Search models. The sale price prediction is also helpful for property buyers or sellers.

To better manage risks for new property flippers, we recommend the Reno Flip. The reno flip, in which a property flipper improves undervalued properties with renovations and/or cosmetic changes, is deemed less risky. 

Thus, our recommendations will focus on features that are more likely to increase property value when renovated, and which features to de-prioritise.

**Data Cleaning**

Dropped columns -  
1) 'Mo Sold', 'Yr Sold' because these are datetime elements that will mess up the data later when I do a train-test split. Also because of the nature of our business which is to encourage clients to buy/ sell property for a gain by looking into the features of a property, I am leaving out such time based elements to rule out other influencing factors that are beyond our control.   

2) 'Sale Type' because it is a factor based on the US housing law that will require deeper research to check if it has any effect on the sale price. For now, I think it's wiser to leave it out in the analysis.  

3) 'Pool QC' because there are far too many missing values to be of any use in the analysis. 

4) 'Garage Type', 'Garage Yr Built', 'Garage Finish', 'Garage Cars' in order to reduce multicolinearity. 

Created new columns - 

5) 'Bsmt Liv Area' which is the liveable space in the basement gotten by subtracting the basement unfinished sf from the total basement sf.

6) 'Garage' --> 0 for no garage and 1 for if there is a garage.

Imputed zero for -

7) 'Alley', 'Fence', 'Fireplace Qu', 'Mas Vnr Type' and 'Mas Vnr Area' since the null cells indicate that there is none of the feature.

Imputed mean for -

8) 'Lot Frontage' since this is crucial information in determining the saleprice.



**Data Dictionary**

|Feature|Type|Dataset|Description|
|---|---|---|---|
|id|int|df|The transaction id of the sale of the house.| 
|pid|int|df|Parcel identification number. | 
|ms_subclass|int|df|Identifies the type of dwelling involved in the sale.| 
|ms_zoning|object|df|Identifies the general zoning classification of the sale.| 
|lot_frontage|float|df|Linear feet of street connected to property.| 
|lot_area|int|df|Lot size in square feet. | 
|street|object|df|Type of road access to property.| 
|lot_shape|object|df|General shape of property.| 
|land_contour|object|df|Flatness of the property.|
|utilities|object|df|Type of utilities available. | 
|lot_config|object|df|Lot configuration.| 
|land_slope|object|df|Slope of property.| 
|neighborhood|object|df|Physical locations within Ames city limits.|
|condition_1|object|df|Proximity to various conditions.| 
|condition_2|object|df|Proximity to various conditions (if more than one is present).|
|bldg_type|object|df|Type of dwelling. | 
|house_style|object|df|Style of dwelling.| 
|overall_qual|int|df|Rates the overall material and finish of the house.| 
|overall_cond|int|df|Rates the overall condition of the house.|
|year_built|int|df|Original construction date.| 
|year_remod/add|int|df|Remodel date (same as construction date if no remodeling or additions). | 
|roof_style|object|df|Type of roof.| 
|roof_matl|object|df|Roof material.| 
|exterior_1st|object|df|Exterior covering on house.| 
|exterior_2nd|object|df|Exterior covering on house (if more than one material).| 
|mas_vnr_type|object|df|Masonry veneer type.| 
|mas_vnr_area|float|df|Masonry veneer area in square feet.| 
|exter_qual|object|df|Evaluates the quality of the material on the exterior.|
|exter_cond|object|df|Evaluates the present condition of the material on the exterior. | 
|foundation|object|df|Type of foundation.| 
|bsmt_qual|object|df|Evaluates the height of the basement.| 
|bsmt_cond|object|df|Evaluates the general condition of the basement.|
|bsmt_exposure|object|df|Refers to walkout or garden level walls.| 
|heating|object|df|Type of heating.|
|heating_qc|object|df|Heating quality and condition. | 
|central_air|object|df|Central air conditioning.| 
|electrical|object|df|Electrical system.| 
|1st_flr_sf|int|df|First Floor square feet.|
|2nd_flr_sf|int|df|Second floor square feet.| 
|low_qual_fin_sf|int|df|Low quality finished square feet (all floors). | 
|gr_liv_area|int|df|Above grade (ground) living area square feet.| 
|bsmt_full_bath|float|df|Basement full bathrooms.| 
|bsmt_half_bath|float|df|Basement half bathrooms.| 
|full_bath|int|df|Full bathrooms above grade.| 
|half_bath|int|df|Half baths above grade.| 
|bedroom_abvgr|int|df|Bedrooms above grade (does NOT include basement bedrooms).| 
|kitchen_abvgr|int|df|Kitchens above grade.|
|kitchen_qual|object|df|Kitchen quality. | 
|totrms_abvgrd|int|df|Total rooms above grade (does not include bathrooms).| 
|functional|object|df|Home functionality (Assume typical unless deductions are warranted).| 
|fireplaces|int|df|Number of fireplaces.|
|fireplace_qu|object|df|Fireplace quality.| 
|garage_area|float|df|Size of garage in square feet.|
|garage_qual|object|df|Garage quality.| 
|garage_cond|object|df|Garage condition. 
|paved_drive|object|df|Paved driveway.| 
|wood_deck_sf|int|df|Wood deck area in square feet.|
|open_porch_sf|int|df|Open porch area in square feet.| 
|enclosed_porch|int|df|Enclosed porch area in square feet.|
|3ssn_porch|int|df|Three season porch area in square feet.| 
|screen_porch|int|df|Screen porch area in square feet.|
|pool_area|int|df|Pool area in square feet. | 
|fence|object|df|Fence quality.| 
|misc_feature|object|df|Miscellaneous feature not covered in other categories.| 
|misc_val|int|df|Value of miscellaneous feature.|
|saleprice|int|df|Sale price. | 
|bsmt_liv_area|float|df|Basment living area (Total basement sf - Basment unfinished sf).| 
|have_alley|int|df|Whether the house has an alley or not.| 
|garage|int|df|Whether the house has a garage or not.|

**EDA**

In visualizing the data, I used stripplots and boxplots to detect outliers which were henceforth removed.   
With there being too many feature columns, the heatmap was not friendly to the eye, so I used an alternative to gather the same crucial information which proved to be a good precursor to helping me see what features to keep a lookout for. 
There being many non-numerical columns, the initial pickout from Pearson correlation coeff simply highlighted the usual suspects such as living space area, quality of house as a whole etc. More needed to be done to sieve out more contributing features to the saleprices.  
Although the histogram showed the saleprice being right skewed, I attempted to normalize the data but left it as is because I knew later on that I'd be standard scaling my variables for modelling anyway. 

**Preprocessing and Modeling** 

Along the way, I dropped columns that were closely correlated to other columns ie. basement 1 sf, basement 2 sf just so that I could reduce multicolinearity which would have impaired my model.

There were also many ordinal columns which had to be assigned numerical values before any further action could be taken. 

Similarly there were many nominal columns which had to be one-hot encoded subsequently. The main one to highlight is that of 'neighborhood' which didn't make sense to be dummified, so I grouped them based on their median prices. 

In modeling, I did up LR, LassoCV, RidgeCV as well as tried my hand on GridSearch. Because of the spectrum of scales we were dealing with, it was a must to carry out standard scaling on our variables. 


**Evaluation and Conceptual Understanding** 

With the exception of LR since this number of features would have meant LR is grossly underfitting, the rest of the models were quite alright as they produced decent R2 results for both Lasso and Ridge, showing that the models have trained well in explaining ~91% of the training data and tested equally well to account for ~89% of the test set. Coupled with reasonable RMSE scores, I think the models did rather well. Between the two, Ridge reported marginally better scores.  

I submitted both my Lasso and Ridge predictions on Kaggle with the latter drawing a decent score so I presume the predictions are within an acceptable range of tolerance. 


**Conclusion and Recommendations** 

From the top features gathered from both the Ridge and Lasso models, I collated a combined list to get the best of both worlds. It wasn't surprising to find out that features such as ground living area, basement living area, 1st floor sq ft, 2nd floor sq ft influenced the selling price greatly since it is common knowledge that the bigger the size of the house, the more expensive it will be. More helpful information from the list include being able to tell which neighborhood's houses generated a higher price and the kind of exterior finishings that can potentially mark up the selling price of the house. These will be useful information for our potential buyers when they are deciding what type of house to buy to in turn sell when the time is ripe for a good gain. 

Further down the list, I can pick out other features that contribute to the selling price of the house such as the quality of the kitchen's finishings, that cement board (+ve coef) is preferred to wood siding (-ve coef) for exterior of the house and wood shingles for the roof's materials is ideal. Such details will be crucial information to sellers who can consider sprucing up their homes in specific areas before putting them up for sale at a higher price. 

As a closing, I will advise my clients to always come to me for consultation on the latest model aka our winning formula as my team will constantly update the model with the latest datapoints in order to we present to clients the most up-to-date model and corresponding list of features to look out for.


### References
1. Many thanks to Jesse Villines for the detailed breakdown of how he handled this set of housing data without which I may not have known how to tackle some nitty gritty details.  
[Part 1](https://medium.com/mlearning-ai/a-thorough-dive-into-the-ames-iowa-housing-dataset-part-1-of-5-7205093a5a53)  
[Part 2](https://medium.com/mlearning-ai/a-thorough-dive-into-the-ames-iowa-housing-dataset-part-2-of-5-3e24ea276e1c)  
[Part 3](https://medium.com/mlearning-ai/a-thorough-dive-into-the-ames-iowa-housing-dataset-part-3-of-4-2c00e0a0eacf)  
[Part 4](https://medium.com/mlearning-ai/a-thorough-dive-into-the-ames-iowa-housing-dataset-part-4-of-4-e127321885da)  

2. [Alvin T.Tan](https://towardsdatascience.com/wrangling-through-dataland-modeling-house-prices-in-ames-iowa-75b9b4086c96) also shared very insightful viewpoints which gave me alternative perspectives when handling certain aspects of this dataset.

3. In making sure to understand more about property flipping, we researched online for the [Singapore market](https://www.propertyguru.com.sg/property-guides/property-flipping-singapore-boomer-millennial-28396) as well as the US markets([article 1](https://en.wikipedia.org/wiki/United_States_housing_bubble), [article 2](https://www.investopedia.com/articles/mortgages-real-estate/08/house-flip.asp), [article 3](https://www.investopedia.com/terms/f/flipping.asp)). We initially wanted to bring the context back to Singapore but realised that without sufficient data for the Singapore market, it would not be convincing hence we stayed within the US market of Ames, Iowa.


