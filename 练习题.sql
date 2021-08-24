-- 单表查询练习
-- 1.查询出部门编号为30的所有员工
SELECT * FROM t_employees WHERE deptno=30;


-- 2.查询所有销售员的姓名、编号和部门编号
SELECT ename,empno,deptno FROM t_employees;


-- 3.查询所有job为salesman的销售员、编号和部门编号
SELECT ename,empno,deptno FROM t_employees WHERE job="salesman";


-- 4.找出奖金高于工资的员工
SELECT * FROM t_employees WHERE comm>sal;


-- 5.找出奖金高于工资60%的员工
SELECT * FROM t_employees WHERE comm>sal * 0.6;


-- 6.找出部门编号为10中所有经理，和部门编号为20中所有销售员的详细资料
SELECT * FROM t_employees WHERE (deptno = 10 AND job = "manager") OR (deptno = 20 AND job = "salesman");


-- 7.找出部门编号为10中所有经理，部门编号为20中所有员工详细资料
 SELECT * FROM t_employees WHERE (deptno = 10 AND job = "manager") OR (deptno = 20 AND sal<20000);
 
 
-- 8.无奖金或者奖金低于1000的员工
SELECT * FROM t_employees WHERE comm IS 'NULL' OR comm<1000;


-- 9.查询2000年入职的员工
SELECT * FROM t_employees WHERE hiredate LIKE '1981%';


-- 10.查询所有员工详细信息，用编号升序排序
SELECT * FROM t_employees ORDER BY empno ASC;


-- 查询所有员工信息，按照薪资从高到低进行排序
SELECT * FROM t_employees ORDER BY sal DESC;


-- 查询所有员工详细信息，用工资降序排序，如果工资相同，使用入职日期升序排序
SELECT * FROM t_employees ORDER BY sal DESC,hiredate ASC;


-- 12.查询每个部门的平均工资   group by 字段    avg（字段）
SELECT deptno,AVG(sal) FROM t_employees GROUP BY deptno;
 
 
-- 13.查询每个部门的雇员数量   count （字段）
SELECT deptno, COUNT(empno) FROM t_employees GROUP BY deptno;
 
 
-- 14.查询每种工作的最高工资max()、最低工资min()、人数count()
SELECT job, MAX(sal),MIN(sal),COUNT(*) FROM t_employees GROUP BY job;
 
 
-- 15.查询名字由四个字母组成的员工
SELECT * FROM t_employees WHERE ename LIKE "____";


-- 多表查询练习
/*
1. 查出至少有一个员工的部门。显示部门编号、部门名称、部门位置、部门人数。
列：d.deptno, d.dname, d.loc, 部门人数
表：dept d, emp e
条件：e.deptno=d.deptno
*/
SELECT d.*, z1.cnt 
FROM dept d, (SELECT deptno, COUNT(*) cnt FROM emp GROUP BY deptno) z1
WHERE d.deptno = z1.deptno

/*
3. 列出所有员工的姓名及其直接上级的姓名。
列：员工姓名、上级姓名
表：emp e, emp m
条件：员工的mgr = 上级的empno
*/
SELECT s.ename,t.ename
FROM t_employees s,t_employees t
WHERE s.`MGR` = t.`empno`


/*
4. 列出受雇日期早于直接上级的所有员工的编号、姓名、部门名称。
列：e.empno, e.ename, d.dname
表：emp e, emp m, dept d
条件：e.hiredate<m.hiredate
思路：
1. 先不查部门名称，只查部门编号!
列：e.empno, e.ename, e.deptno
表：emp e, emp m
条件：e.mgr=m.empno, e.hiredate<m.hireadate
*/
SELECT e.empno, e.ename, e.deptno
FROM emp e, emp m
WHERE e.mgr=m.empno AND e.hiredate<m.hiredate


SELECT e.empno, e.ename, d.dname
FROM emp e, emp m, dept d
WHERE e.mgr=m.empno AND e.hiredate<m.hiredate AND e.deptno=d.deptno



/*
5. 列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门。
列：* 
表：emp e, dept d
条件：e.deptno=d.deptno
*/
SELECT *
FROM emp e RIGHT OUTER JOIN dept d
ON e.deptno=d.deptno

/*
7. 列出最低薪金大于15000的各种工作及从事此工作的员工人数。
列：job, count(*)
表：emp e
条件：min(sal) > 15000
分组：job
*/
SELECT job, COUNT(*)
FROM emp e
GROUP BY job
HAVING MIN(sal) > 15000


/*
8. 列出在销售部工作的员工的姓名，假定不知道销售部的部门编号。
列：e.ename
表：emp
条件：e.deptno=(select deptno from dept where dname='销售部')
*/

SELECT *
FROM emp e
WHERE e.deptno=(SELECT deptno FROM dept WHERE dname='销售部')



/*
9. 列出薪金高于公司平均薪金的所有员工信息，所在部门名称，上级领导，工资等级。
列：* 
表：emp e
条件：sal>(查询出公司的平均工资)
*/
SELECT e.*, d.dname, m.ename, s.grade
FROM emp e, dept d, emp m, salgrade s
WHERE e.sal>(SELECT AVG(sal) FROM emp) AND e.deptno=d.deptno AND e.mgr=m.empno AND e.sal BETWEEN s.losal AND s.hisal

---------------

SELECT e.*, d.dname, m.ename, s.grade
FROM 
  emp e LEFT OUTER JOIN dept d ON e.deptno=d.deptno
        LEFT OUTER JOIN emp m ON e.mgr=m.empno
        LEFT OUTER JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
WHERE e.sal>(SELECT AVG(sal) FROM emp)


SELECT * FROM emp;
SELECT * FROM dept;
SELECT * FROM salgrade;



/*
10.列出与clack从事相同工作的所有员工及部门名称。
列：e.*, d.dname
表：emp e, dept d
条件：job=(查询出庞统的工作)
*/

SELECT e.*, d.dname
FROM emp e, dept d
WHERE e.deptno=d.deptno AND job=(SELECT job FROM emp WHERE ename='庞统')



/*
11.列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金、部门名称。
列：e.ename, e.sal, d.dname
表：emp e, dept d
条件；sal>all (30部门薪金)
*/
SELECT e.ename, e.sal, d.dname
FROM emp e, dept d
WHERE e.deptno=d.deptno AND sal > ALL (SELECT sal FROM emp WHERE deptno=30)

























