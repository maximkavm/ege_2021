#include <iostream>
#include <string>
#include <cmath>

using namespace std;

string decTo(int x, int base, int len=0) {
    string s;
    while (x > 0) {
        s = to_string(x % base) + s;
        x /= base;
    }
    while (s.size() < len) s = '0' + s;
    return s;
}

int main() {
    //int s = 4;
    for (int s=1; s<=41; s++) {
    bool b = false;
    for (int i=0; i < pow(4, 2); i++) {
        int x = 7;
        int y = s;
        string st = decTo(i, 4, 2);
        int sumPetya, sumVanya;
        for (int j = 0; j < st.size(); j++) {
            if (st[j]=='0') x++;
            if (st[j]=='1') y++;
            if (st[j]=='2') x*=2;
            if (st[j]=='3') y*=2;
            if (j==0)
                sumPetya = x + y;
            if (j==1)
                sumVanya = x + y;
        }
        //cout << x << " " << y << " ";
        //cout << st << "\n";
        if ((sumVanya >= 49) && (sumPetya < 49)) b =true;
    }
    if (b)
        cout << s << " Yes\n";
    else
        cout << s << " No\n";
    }

    return 0;
}
