from extract import extract_data
from transform import transform_data
from load import save_to_csv

QUERY = "SELECT * FROM student"


def main():
    """Run the ETL process."""
    df = extract_data(QUERY)
    trans_data = transform_data(df)
    save_to_csv(trans_data, "student_data.csv")


if __name__ == "__main__":
    main()
