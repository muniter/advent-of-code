#include <stdio.h>
#include <stdlib.h>
#define SIZE 4
int ind(int i)
{
  return abs(SIZE * (i < 0) + i - SIZE * (i >= SIZE));
  // return (SIZE + (i % SIZE)) % SIZE;
}

int main (int argc, char *argv[])
{
  int values[SIZE] = {-1, -1, -1, -1};
  int increments = 0;
  int decrements = 0;
  int previous = 0;
  int current = 0;
  char charint[10];
  FILE *fp = fopen("input", "r");
  int slider = 0;
  int count = 0;
  int ok = 0;
  for (count = 0; fgets(charint, 10, fp) != NULL; count++) {
    ok = count > SIZE;
    values[slider] = atoi(charint);
    current = values[slider] + values[ind(slider - 1)] + values[ind(slider - 2)];
    previous = values[ind(slider - 1)] + values[ind(slider - 2)] + values[ind(slider - 3)];
    increments += ok * current > previous;
    decrements += ok * current > previous;
    slider++;
    slider -= (slider == SIZE) * SIZE;
  }
  printf("At the end the counts %d\n", count);
  printf("Increments: %d, decrements: %d\n", increments, decrements);
  return 0;
}
