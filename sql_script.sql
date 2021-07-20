
drop table employees;
create table employees (
	emp_id int primary key,
	emp_name varchar(20),
	emp_username varchar(20) not null,
	emp_password varchar(20) not null
	
);


drop table managers;
create table managers(
	manager_id int,
	manager_name varchar(20) primary key,
	manager_username varchar(20) not null,
	manager_password varchar(20) not null
);


drop table reimb_report;
create table reimb_report(
	emp_id int references employees(emp_id) on delete cascade,
	request_id int,
	item varchar(20),
	item_cost numeric(5,2),
	purpose varchar(90),
	req_status varchar(20),
	manager_name varchar(30) references managers(manager_name)
);

select item from reimb_report where emp_id = 1;
delete from employees where emp_id = 2;


-- CREATE VIEW

CREATE VIEW reimb_stats as 	
SELECT
    employees.emp_id,
 	SUM (reimb_report.item_cost) AS total,
 	employees.emp_name
FROM
    employees
full join reimb_report 
    ON reimb_report.emp_id =employees.emp_id
group by employees.emp_id
order by total desc;