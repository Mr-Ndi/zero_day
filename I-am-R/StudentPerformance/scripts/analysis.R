# Load required libraries
library(readr)
library(dplyr)
library(ggplot2)

# Prepare output directories
output_dir <- "../outputs"
plot_dir <- file.path(output_dir, "plots")

if (!dir.exists(plot_dir)) {
  dir.create(plot_dir, recursive = TRUE)
}

# Load data
data <- read_csv("../data/students_performance.csv")

# Clean data
clean_data <- na.omit(data)
prepared_data <- clean_data %>%
  filter(test_preparation != "none")

# Summary
avg_scores_by_gender <- prepared_data %>%
  group_by(gender) %>%
  summarise(across(ends_with("_score"), mean), .groups = "drop")

# Save summary
write_csv(avg_scores_by_gender, file.path(output_dir, "summary.csv"))

# Plot and save
plot <- ggplot(prepared_data, aes(x = math_score)) +
  geom_histogram(binwidth = 5, fill = "steelblue", color = "white") +
  labs(title = "Distribution of Math Scores", x = "Math Score", y = "Count")

ggsave(file.path(plot_dir, "score_distribution.png"), plot = plot, width = 8, height = 6)
