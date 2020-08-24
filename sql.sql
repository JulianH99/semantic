CREATE PROCEDURE proc_name(my_param_name varchar = null, another_param_name int = 1)
BEGIN
    select name as full_name from
     my_table where cond = '' and col = '';
 END