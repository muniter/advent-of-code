#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[])
{
  int pre = -1;  // Sentinel value
  int curr = -1;
  int increments = 0;
  int decrements = 0;
  char charint[10];
  FILE *fp = fopen("input", "r");
  while (fgets(charint, 10, fp) != NULL) {
    pre = curr;
    curr = atoi(charint);
    increments += (curr > pre) * (pre != -1);
    decrements += (curr < pre) * (pre != -1);
  }
  printf("Increments: %d, decrements: %d\n", increments, decrements);
  return 0;
}
