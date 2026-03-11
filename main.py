from src.load_data import load_data
from src.clean_data import clean_data
from src.feature_engineering import create_features
from src.analysis import sales_summary, sales_by_region, sales_by_category, top_products
from src.report import generate_report


def main():

    path = "data/superstore_final_dataset (1).csv"

    df = load_data(path)

    df = clean_data(df)

    df = create_features(df)

    total, avg, std = sales_summary(df)

    region = sales_by_region(df)

    category = sales_by_category(df)

    top = top_products(df)

    generate_report(total, avg, std, region, category, top)


if __name__ == "__main__":
    main()