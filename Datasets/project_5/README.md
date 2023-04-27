# Effects of Loan Features on the Estimated Return
## by Luiz Iurk


## Dataset

> The data set consists of 113937 records with several atributes about borrowers and loans. Most of the attributes are related to the borrowers profile, such as monthly income, loan term, loan range, customer rating, etc.
> The dataset is available [here](https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv) and the data dictionary explaining each one of the fields can be fetched [here](https://docs.google.com/spreadsheets/d/1gDyi_L4UvIrLTEC6Wri5nbaMmkGmLQBk-Yx3z0XDEtI/edit#gid=0)


## Summary of Findings

> In the preliminary studies I found ou that the Estimated Return has an unimodal distribution that the loan amounts showed 5k pace spikes. The big majoroty of the customers have a monthly income below 30k and the preferred term is of 36 months with the intention of, in most of the cases, consolidate debts.<br>
Further exploration showed that we have a negative and weak (according to Pearson's Range) correlation coefficient between the loaned amount and the estimated return. the same with happens with the Monthly Income.<br>
In other hand, the income and loaned amount are positively correlated, yet weak. But it makes sense to think that, the more you earn, the more you borrow.<br>
The estimated return decreases the higher the borrower rating is.<br>
The borrower state doesn't show big impact on the estimated return. But loan category, despite showing low impact, has shown interesting behaviors, depending on the customer employment status. So, I picked this feature in particular, in order to help to design potential products for the bank.  <br>
The proportional analysis showed us that borrowers from the rating level B and C lend mononey in longer terms, if compared to the other classes. <br>
When it comes to employment status, the proportion is roughly the same to each class, except that employed borrowers lend money with higher terms. This can be explained by the fact that these people have the feeling of having the comfort of a guaranteed income at the end of the month, while part time or self-employed don't dare to take risks at a long term.
In the absolute plot was not easy to see, but the in the proportional one is clear to see that Not employed borrowers are mostly in the High Risk Group of ProperRating. In other hand, Full-Time and Employed are in more concenrated in the highest ratings.<br>
> Going deeper in the multivariate exploration, it was becoming clearer that the return decreases with the increasing of the prosper rating. The curious thing happens in the range of high risk (HR). This Prosper Rating group shows a positive trend in the correlation and an estimated return very similar (sometimes bigger) than the higher ratings.
So, despite having higher risk, loans for this niche of customer can be very profitable.
This is reinforced when we relate the return and prosper rating towards the term and category. For the same category loan, an HR customer can have up to 2 times more return than an AA customer.
> Splitting the group by incomes lower an higher than $10k we can provide enough evidences that, the bank can have good returns if they invest in customer of higher risk and lower incomes. This is because the number of delinquencies is relatively low as well.


## Key Insights for Presentation

> Despite having many features to explore (more than 50), some of them are indirectly originated from another in the dataset. So I focused in those that are primarily used for financial planning: Time, Amount and Risk, which translated to our dataset are term, original loan amount, prosper rating.
I started by showing the distribution of the estimated return and the original loan amounts. Then, I showed the relationship pairs of the estimated return and the original loan amount and the return vs. borrower rating. 
In the sequence, it was investigated the effect of the rating on the pair estimated return and the original loan amount. Lastly, I compared the term and the loan category with the rating and the estimated return.