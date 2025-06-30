# Load required libraries
library(readr)
library(dplyr)
library(ggplot2)

# Load the dataset
data <- read_csv("../data/students_performance.csv")  # go up one directory to find data

# View the structure and summary
glimpse(data)
summary(data)

# Remove rows with NA
clean_data <- na.omit(data)

# Remove rows where test_preparation is "none"
prepared_data <- clean_data %>%
  filter(test_preparation != "none")

# Calculate average scores by gender
avg_scores_by_gender <- prepared_data %>%
  group_by(gender) %>%
  summarise(across(ends_with("_score"), mean))

print(avg_scores_by_gender)

# Plot math score distribution
ggplot(prepared_data, aes(x = math_score)) +
  geom_histogram(binwidth = 5, fill = "steelblue", color = "white") +
  labs(title = "Distribution of Math Scores", x = "Math Score", y = "Count")
