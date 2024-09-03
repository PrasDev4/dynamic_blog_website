DECLARE
    a NUMBER := 1;
BEGIN
    dbms_output.put_line('Program started'); 
    LOOP
        dbms_output.put_line(a); 
        a := a + 1;
        EXIT WHEN a > 5;
    END LOOP;

    WHILE a > 1 LOOP
        a := a - 1;
        dbms_output.put_line(a);
    END LOOP;

    dbms_output.put_line('Program completed');
END;
