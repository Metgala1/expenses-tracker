def add_expenses(expenses, amount, category) :
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses) :
    for expense in expenses :
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses) :
    return sum(map(lambda expense : expense['amount'], expenses))
