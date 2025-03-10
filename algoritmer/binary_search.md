FUNCTION binary_search(liste, tall)
    SET liste TO sortert liste
    WHILE liste ikke er tom
        SET m TO midterste element
        IF m EQUAL TO tall
            RETURN True
        ELSE IF tall GREATER THAN m
            SET liste TO delen av listen til høyre for m
        ELSE
            SET liste TO delen av listen til venstre for m
        ENDIF
    ENDWHILE
    RETURN False
ENDFUNCTION