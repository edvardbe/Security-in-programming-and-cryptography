#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Replace &, <, > with &amp;, &lt;, &gt; in a new string
char* replace_amp_lt_gt(const char* input) {
    size_t len = strlen(input);
    // Worst case: every char replaced by 5 chars ("&amp;")
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

int main() {
    printf("Ampersand:\n");
    char* amp_org = "What the he&&y";
    printf("Original: %s\n", amp_org);
    char* amp_alt = replace_amp_lt_gt(amp_org);
    printf("Altered: %s\n\n", amp_alt);
    free(amp_alt);

    printf("Less than:\n");
    char* lt_org = "What the he<<y";
    printf("Original: %s\n", lt_org);
    char* lt_alt = replace_amp_lt_gt(lt_org);
    printf("Altered: %s\n\n", lt_alt);
    free(lt_alt);

    printf("Greater than:\n");
    char* gt_org = "What the he>>y";
    printf("Original: %s\n", gt_org);
    char* gt_alt = replace_amp_lt_gt(gt_org);
    printf("Altered: %s\n\n", gt_alt);
    free(gt_alt);

    return 0;
}