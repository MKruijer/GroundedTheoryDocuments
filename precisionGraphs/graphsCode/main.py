import numpy as np
import matplotlib.pyplot as plt
import psycopg as psycopg
from scipy.optimize import curve_fit
from scipy.stats import linregress


def get_precision_values_from_database(table_name, orderby_column_name, cursor):
    query = f"""
            SELECT pattern FROM {table_name}
            order by {orderby_column_name} desc
            limit 100;
            """
    cursor.execute(query)
    iter1patterns = cursor.fetchall()
    pattern_values = [pattern_dict["pattern"] for pattern_dict in iter1patterns]

    precision_values = [0.0] * len(pattern_values)
    amount_of_related = 0
    for i in range(1, len(pattern_values) + 1):
        if pattern_values[i - 1] > 0:
            amount_of_related += 1
        precision_values[i - 1] = amount_of_related / i
    return precision_values


# Function to plot the arch_issue precision graph
def plot_arch_issue_precision(iter0_arch_issue_precision, iter1_arch_issue_precision,
                              iter2_arch_issue_precision, iter3_arch_issue_precision,
                              iter4_arch_issue_precision):
    # Generate x-values for the data entry indices (assuming all lists have the same length)
    x_values = np.arange(1, len(iter1_arch_issue_precision) + 1)

    # Set the figure size
    plt.figure(figsize=(10, 6))  # Adjust the width and height as needed

    # Plot each list with a different color and label
    plt.plot(x_values, iter0_arch_issue_precision, label='Iter0', color='#9400D3')
    plt.plot(x_values, iter1_arch_issue_precision, label='Iter1', color='g')
    plt.plot(x_values, iter2_arch_issue_precision, label='Iter2', color='c')
    plt.plot(x_values, iter3_arch_issue_precision, label='Iter3', color='y')
    plt.plot(x_values, iter4_arch_issue_precision, label='Iter4', color='k')

    # Set the y-axis limits (if needed)
    plt.ylim(0.0, 1.1)

    plt.xlabel('Pair Index')
    plt.ylabel('Precision')
    plt.title('Precision Graph for Architectural Issue All Email pairs')
    plt.legend()
    plt.show()


# Function to plot the arch_email precision graph
def plot_arch_email_precision(iter0_arch_email_precision, iter1_arch_email_precision,
                              iter2_arch_email_precision, iter3_arch_email_precision):
    # Generate x-values for the data entry indices (assuming all lists have the same length)
    x_values = np.arange(1, len(iter1_arch_email_precision) + 1)

    # Set the figure size
    plt.figure(figsize=(10, 6))  # Adjust the width and height as needed

    # Plot each list with a different color and label
    plt.plot(x_values, iter0_arch_email_precision, label='Iter0', color='#FF8C00')
    plt.plot(x_values, iter1_arch_email_precision, label='Iter1', color='b')
    plt.plot(x_values, iter2_arch_email_precision, label='Iter2', color='r')
    plt.plot(x_values, iter3_arch_email_precision, label='Iter3', color='m')

    # Set the y-axis limits (if needed)
    plt.ylim(0.0, 1.1)

    plt.xlabel('Pair Index')
    plt.ylabel('Precision')
    plt.title('Precision Graph for Architectural Email All Issue pairs')
    plt.legend()
    plt.show()


def main_function():
    with psycopg.connect(
            host="localhost",
            dbname="relationsDB",
            user="postgres",
            password="UnsavePassword",
            port=5432) as connection:
        cursor = connection.cursor(row_factory=psycopg.rows.dict_row)
        iter0_arch_email_precision = get_precision_values_from_database("iter0_expanded_arch_emails_all_issues", "similarity", cursor)
        iter0_arch_issue_precision = get_precision_values_from_database("iter0_expanded_arch_issues_all_emails", "similarity", cursor)
        iter1_arch_email_precision = get_precision_values_from_database("iter1_analysis_unique_pairs_arch_emails_all_issues", "similarity", cursor)
        iter1_arch_issue_precision = get_precision_values_from_database("iter1_analysis_unique_pairs_arch_issues_all_emails", "similarity", cursor)
        iter2_arch_email_precision = get_precision_values_from_database("iter2_unique_filtered_sim_arch_emails_all_issues", "similarity", cursor)
        iter2_arch_issue_precision = get_precision_values_from_database("iter2_unique_filtered_sim_arch_issues_all_emails", "similarity", cursor)
        iter3_arch_email_precision = get_precision_values_from_database("iter3_average_similarity_arch_emails_all_issues", "average_similarity", cursor)
        iter3_arch_issue_precision = get_precision_values_from_database("iter3_average_similarity_arch_issues_all_emails", "average_similarity", cursor)
        iter4_arch_issue_precision = get_precision_values_from_database("iter4_average_similarity_arch_issues_all_emails", "average_similarity", cursor)

    plot_arch_issue_precision(iter0_arch_issue_precision, iter1_arch_issue_precision,
                              iter2_arch_issue_precision, iter3_arch_issue_precision,
                              iter4_arch_issue_precision)

    plot_arch_email_precision(iter0_arch_email_precision, iter1_arch_email_precision,
                              iter2_arch_email_precision, iter3_arch_email_precision)


if __name__ == '__main__':
    main_function()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
