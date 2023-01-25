# parser_calorie_table
This is a simple parser of the calorie table of products from the site https://health-diet.ru written in Python, which receives data from each product category and stores it in json and csv.

### Installation

* Clone the repository using the command in the terminal `git clone https://github.com/alexeyvershinin/parser_calorie_table.git` or download the archive from the [link](https://github.com/alexeyvershinin/parser_calorie_table/archive/refs/heads/master.zip)

* Install all the necessary dependencies from the file `requirements.txt` using command `pip install -r requirements.txt`

* Go to the folder with the downloaded repositories and run the `main.py` file in the terminal with the command `python main.py` or in your favorite IDE

#### After executing the script, you will receive the following files:

* `all_categories_dict.json` list of all product categories with links to them

* `data` directory with `json` and `csv` files that contain data on the caloric content of products
