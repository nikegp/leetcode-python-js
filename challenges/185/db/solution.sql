WITH RankedEmployee AS (SELECT
                          name AS Employee,
                          salary AS Salary,
                          departmentId,
                          DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS SalaryRank
                        FROM
                          Employee)
SELECT
  Department.name AS Department,
  RankedEmployee.Employee,
  RankedEmployee.Salary
FROM
  RankedEmployee
  INNER JOIN Department
  ON Department.id = RankedEmployee.departmentId
WHERE
  RankedEmployee.SalaryRank <= 3