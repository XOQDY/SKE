#include <iostream>
#include <stack>

using namespace std;

int main()
{
    stack<double> operands;
    string expression;

    while (cin >> expression and expression.at(0) != '=')
    {
        if (!(expression.at(0) >= '0' && expression.at(0) <= '9'))
        {
            double back;
            double first;
            back = operands.top();
            operands.pop();
            first = operands.top();
            operands.pop();

            if (expression.at(0) == '+')
                operands.push(first + back);
            else if (expression.at(0) == '-')
                operands.push(first - back);
            else if (expression.at(0) == '*')
                operands.push(first * back);
            else
                operands.push(first / back);
        } else
            operands.push(stod(expression));
    }
    printf("%.4f", operands.top());
}
