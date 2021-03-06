Function of the script:
Pull in the potential audience size for each Facebook Ad Set.
The audience size are then grouped by campaigns (it is divided by market in default)


What is required:
Python 3.6 & install modules: facebook_business, openpyxl

The ad sets on Facebook must be name in this pattern with denominator (Orders can be different):
Example:
Market_Targeting_Feature1_Feature2_Feature3

Before Running the script:
1. Download the reach-estimate folder
2. Export selected campaigns on ads manager to excel.
3. Remove Duplicates on an ad set ID level, so each row will be a unique ad set.
4. Fill in the app ids, app secret and access token. (To authenticate you have access to the account)

Then RUN THE SCRIPT.
5. After pressing running the script, drag and drop the exported excel file, press enter.
6. It will run and populate on to the excel file.
7. You should be prompted with a message showing where the file is saved.
8. Open the excel newly created excel file.
9. Set your Bench Mark CPM, Frequency Goal & Campaign Period at Column L(Reach Tab)
10. State the market and targeting slot from your naming conventions at Column L(Reach Tab)
    From the example above, market will be 1, and targeting will be 2
11. Input all markets in the table below at Column K(Reach tab).
12. Input Clients fixed budget in Column N (Reach tab) per market to know the scaled budget to put on platform.
13. Input all targetings in the Column B (Planning tab), for a more detailed breakdown.

If you are happy with the budgets in Column I (Reach tab), please use the Adset Budget Update Script to update the budget to ads manager.

