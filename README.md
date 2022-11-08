# DevHacksBITpick

https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH


## How to run

0. From the root of the repository
1. Create venv in root of the repository: `python3 -m venv venv`
2. Activate venv: `source ./venv/bin/activate`
3. Install dependencies: `pip3 install -r requirements.txt`
4. Run app: `python3 AtomIc/08-Posts/run.py`
5. Go trough the bellow App workflows
6. Deactivate venv: `deactivate`

## App workflows

### Create a client account
1. From home page go to Register
2. Select Client
3. Fill all fields (ex: client, client@gmail.com, RON, test, test). Click Sign Up
4. Go to Home on the top bar. You should see: Your account has been created! You are now able to log in. Go to Login
5. Insert client@gmail.com, test. Click Login
6. Go to New Post. A message shoulb be displayed: `Your score is 0. Build your trust in order to create a new post!`. This means you need to upload documents in order to get trusted by other users. Go to Account
7. In `Select document` leave `ID Card` filled. Click on Choose file and upload a random PNG file. Click Update. You should see `Your account has been updated!`. Your trust level have increased to 20.
8. Upload a new different document. For each uploaded document the trust level increased by 20.
9. Go to New Post. Fill in the required fields: sum (amount of money to borrow), interest (money willing to additionally give back), pay date, description (your motivation for borrowing money). Click `Post`. A message should be seen: `Your post has been created!` and it should be available at the bottom of the home page.
10. Logout

### Create an investor account
1. Go to Register, click on Investor. Fill in all fields (investor, investor@gmail.com, RON, test, test). Click `Sign Up`
2. Go to Login, fill all fields and click `Login`.
3. When you click on `New Post` you should get `You are an investor` message.
4. On the right side you should see a list with the top users sorted by their trust level.
5. Let's add some money. Go to `Account` on the top bar. Set the value of 100 in `Add money` field and click `Update`. Balance shows `100.0`. Go back to `Home`.
6. Find the post created previously by the client. Click on the sum `50 lei`. Click on the red button on the right: `Pay`. Confirm payment `Yes`. You should see `Payment has been transfered!`. The post have been removed from the home, active posts list.
7. Got o `Account`. The balance dropped to 49: 50 to the client, 1 to the platform as a tax.
8. Logout

### Check status on client account
1. Login using the client account (client@gmail.com, test)
2. Go to `Account`. You would see the post marked as `Funded` and the account Balance is now `50`.
3. Click on the post's title `50 lei` and click on `Pay Back`. You should get: `Insufficient funds (required: 55.00000000000001) . You need an extra 5.000000000000007 ron`
4. Go to account and add `6` lei. Try to `Pay Back` again. You should get `Payment has been transfered!`. The account balance have changed (to -0.65, also getting the platform tax from the client -- A BUG -- not going to fix it :D).
5. Logout

### Check status on investor account
1. Loging as investor. Go to Account
2. Balance is now `104`.
