#include <stdio.h>
  int a[2][12]={{31,28,31,30,31,30,31,31,30,31,30,31},{31,29,31,30,31,30,31,31,30,31,30,31}};
int main(){
  int year,mou,day,sum=0,i=0;
  scanf("%d %d %d",&year,&mou,&day);
  if((year%4==0&&year%100!=0)||year%400==0) {
    i=1;
  }
  for(int j=1;j<mou;j++){
    sum+=a[i][j-1];
  }
  sum+=day;
  printf("%d",sum);
  return 0;
}
