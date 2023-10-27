#include<stdio.h>
int main()
{
int n;
scanf("%d",&n);
n<=0?printf("Enter Valid Lemon"):n==21?printf("Sufficient Lemons"):n>21?printf("Extra lemons u have:%d",n-21):printf("Extra needed: %d",21-n);


}



