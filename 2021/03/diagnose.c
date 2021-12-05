#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  FILE *fp = fopen("input", "r");
  int stats[12] = {0};
  int sentinels[12] = {0b1};
  for (int i = 1; i < 12; i++) {
    sentinels[i] = sentinels[i - 1] << 1;
    stats[i] = 0;
  }
  sentinels[0] = 1;

  int i = 0;
  char strval[15];
  int val = 0;
  int count = 0;
  while (fgets(strval, 14, fp) != NULL) {
    count++;
    val = (int)strtol(strval, NULL, 2);
    for (; i < 12; i++) {
      stats[i] += (sentinels[i] | val) == val;
    }
    i = 0;
  }

  int gamma = 0;
  int epsilon = 0;
  for (i = 0; i < 12; i++) {
    if (stats[i] > count / 2) {
      gamma |= 1 << i;
    } else {
      epsilon |= 1 << i;
    }
  }
  printf("Result: Gamma:%d , Epsilon:%d g*e:%d\n", gamma, epsilon, gamma * epsilon);
  return 0;
}
