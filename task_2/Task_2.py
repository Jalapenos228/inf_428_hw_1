import numpy as np
import unittest


def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def calculate_aggregated_threat_score(department_data, importance_scores):
    weighted_sum = 0
    total_importance = 0
    for (department_scores, importance) in zip(department_data, importance_scores):
        mean_score = np.mean(department_scores)
        weighted_sum += mean_score * importance
        total_importance += importance

    aggregated_score = (weighted_sum / total_importance) if total_importance > 0 else 0
    return min(max(aggregated_score, 0), 90)  # Ensuring score is within 0-90 range


class TestAggregatedThreatScore(unittest.TestCase):

    def test_case_1_similar_departments_equal_importance(self):
        department_data = [
            generate_random_data(30, 5, 100),
            generate_random_data(32, 5, 100),
            generate_random_data(28, 5, 100),
            generate_random_data(29, 5, 100),
            generate_random_data(31, 5, 100)
        ]
        importance_scores = [3, 3, 3, 3, 3]
        result = calculate_aggregated_threat_score(department_data, importance_scores)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 90)

    def test_case_2_high_threat_department(self):
        department_data = [
            generate_random_data(30, 5, 100),
            generate_random_data(32, 5, 100),
            generate_random_data(70, 5, 100),
            generate_random_data(29, 5, 100),
            generate_random_data(31, 5, 100)
        ]
        importance_scores = [3, 3, 3, 3, 3]
        result = calculate_aggregated_threat_score(department_data, importance_scores)
        self.assertGreater(result, 30)

    def test_case_3_high_importance_department(self):
        department_data = [
            generate_random_data(30, 5, 100),
            generate_random_data(32, 5, 100),
            generate_random_data(28, 5, 100),
            generate_random_data(29, 5, 100),
            generate_random_data(70, 5, 100)
        ]
        importance_scores = [3, 3, 3, 3, 5]
        result = calculate_aggregated_threat_score(department_data, importance_scores)
        self.assertGreater(result, 30)

    def test_case_4_varied_department_sizes_and_importance(self):
        department_data = [
            generate_random_data(20, 10, 50),
            generate_random_data(30, 10, 150),
            generate_random_data(25, 5, 120),
            generate_random_data(40, 10, 80),
            generate_random_data(60, 20, 10)
        ]
        importance_scores = [2, 4, 1, 3, 5]
        result = calculate_aggregated_threat_score(department_data, importance_scores)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 90)



if __name__ == '__main__':
    unittest.main()
