/* calculation of simple intrest*/
main()
{
  int p, n;
  float r,si;
  printf("Enter values of p, n, r");
  scanf("%d %d %f, &p, &n, &r");

  si = p * n * r / 100;
  printf("%f\n",si);
}
