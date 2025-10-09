#pragma once
#include <stdlib.h>
#include <string.h>

char* replace_amp_lt_gt(const char* input) {
    if (input == NULL) return NULL;
    
    size_t len = strlen(input);
    size_t max_len = len * 5 + 1;
    char* output = malloc(max_len);
    if (!output) return NULL;

    size_t j = 0;
    for (size_t i = 0; i < len; ++i) {
        if (input[i] == '&') {
            strcpy(&output[j], "&amp;");
            j += 5;
        } else if (input[i] == '<') {
            strcpy(&output[j], "&lt;");
            j += 4;
        } else if (input[i] == '>') {
            strcpy(&output[j], "&gt;");
            j += 4;
        } else {
            output[j++] = input[i];
        }
    }
    output[j] = '\0';
    return output;
}
