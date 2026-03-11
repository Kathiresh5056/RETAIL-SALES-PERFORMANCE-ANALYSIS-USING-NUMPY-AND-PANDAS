import numpy as np

def sales_summary(df):

    total_sales = np.sum(df["Sales"])
    avg_sales = np.mean(df["Sales"])
    std_sales = np.std(df["Sales"])

    return total_sales, avg_sales, std_sales


def sales_by_region(df):

    region_sales = df.groupby("Region")["Sales"].sum()

    return region_sales


def sales_by_category(df):

    category_sales = df.groupby("Category")["Sales"].sum()

    return category_sales


def top_products(df):

    top = df.groupby("Product_Name")["Sales"].sum()

    top_products = top.sort_values(ascending=False).head(10)

    return top_products