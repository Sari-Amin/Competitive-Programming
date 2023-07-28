#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n,q,c=1;
    cin>>n>>q;
    int m =sqrt(n);
    bitset<100000001> Primes;
    
    Primes[0] = 1;
    for (int i = 3; i<= m; i += 2) {
        if (Primes[i / 2] == 0) {
            c++;
            for (int j = 3 * i; j <= n; j += 2 * i)
                Primes[j / 2] = 1;
        }
    }
    for (int i = m+1; i <= n; i++) {
        if (i % 2 == 1 && Primes[i / 2] == 0)
            c++;
    }
    printf("%d\n", c);
    for(int i=0;i<q;i++){
        int a;
        cin>>a;
        if(a==2) printf("%d\n", 1);
        else if(a%2==1 && Primes[a/2]==0)
            printf("%d\n", 1);
        else
            printf("%d\n",0);
    }
    return 0;
}