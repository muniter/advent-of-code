#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{
  int pre = -1;  // Sentinel value
  int curr = -1;
  int increments = 0;
  int decrements = 0;
  char charint[10];
  char *res;
  FILE *fp = fopen("input", "r");
  while (1) {
    res = fgets(charint, 10, fp);
    if (res == NULL) {
      printf("Increments: %d, decrements: %d\n", increments, decrements);
      break;
    }
    pre = curr;
    curr = atoi(charint);
    increments += (curr > pre) * (pre != -1);
    decrements += (curr < pre) * (pre != -1);
  }
  return 0;
}
