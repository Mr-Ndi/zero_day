# Load required libraries
library(readr)
library(dplyr)
library(ggplot2)

# Create necessary output directories if they don't exist
if (!dir.exists("../outputs")) dir.create("../outputs")
if (!dir.exists("../outputs/plots")) dir.create("../outputs/plots")

# Load the dataset
data <- read_csv("../data/students_performance.csv")

# Clean data
clean_data <- na.omit(data)
prepared_data <- clean_data %>%
  filter(test_preparation != "none")

# Summary statistics by gender
avg_scores_by_gender <- prepared_data %>%
  group_by(gender) %>%
  summarise(across(ends_with("_score"), mean), .groups = "drop")

# Save summary to CSV
write_csv(avg_scores_by_gender, "../outputs/summary.csv")

# Create plot
plot <- ggplot(prepared_data, aes(x = math_score)) +
  geom_histogram(binwidth = 5, fill = "steelblue", color = "white") +
  labs(title = "Distribution of Math Scores", x = "Math Score", y = "Count")

# Save plot
ggsave("../outputs/plots/score_distribution.png", plot = plot, width = 8, height = 6)
