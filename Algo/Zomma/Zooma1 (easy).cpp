https://theory.cpe.ku.ac.th/wiki/index.php/Algo_lab/zooma_1
#include <iostream>

using namespace std;

typedef int ValueType;

struct Zuma {
    ValueType ball;
    ValueType color;
    Zuma* next;

    Zuma(ValueType color, ValueType ball, Zuma* next= nullptr)
            : color(color), ball(ball), next(next) {}
};

void insert_ball(Zuma* head, Zuma* insert, int ball_before)
{
    Zuma* temp = head;

    while (temp->ball != ball_before){
        temp = temp->next;
        if (temp->ball == ball_before){
            Zuma* next_temp = temp->next;
            temp->next = insert;
            insert->next = next_temp;
        }
    }
}

void print_list(Zuma* node)
{
    while(node != nullptr) {
        cout << node->ball << endl;
        node = node->next;
    }
}

int main()
{
    int n, m;
    cin >> n >> m;
    int color, ball=1, ball_before;

    Zuma* header = new Zuma(0, 0);
    Zuma* temp = new Zuma(0, 0);
    for (int i=0; i<n; ++i){
        cin >> color;

        if (i==0){
            temp->color = color;
            temp->ball = ball;
            header->next = temp;
        }
        else{
            Zuma* new_temp = new Zuma(color, ball);
            temp->next = new_temp;
            temp = new_temp;
        }
        ++ball;
    }
    for (int j=0; j<m; ++j){
        cin >> color >> ball_before;

        Zuma* new_temp = new Zuma(color, ball);
        insert_ball(header, new_temp, ball_before);
        ++ball;
    }

    print_list(header->next);
}