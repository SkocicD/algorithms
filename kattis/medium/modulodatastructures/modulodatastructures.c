#include <stdio.h>
int main(){
    int N,Q,t,a,b,c;
    scanf("%d %d",&N, &Q);
    long array[N+1];
    for (int i = 0; i < N+1; i++)
        array[i] = 0;
    for (int i = 0; i < Q; i++){
        scanf("%d",&t);
        if (t == 1){
            scanf("%d %d %d", &a, &b, &c);
            for (int j = a; j < N+1; j+=b)
                array[j] += c;
        }else{
            scanf("%d", &a);
            printf("%ld\n", array[a]);
        }
    }

}

