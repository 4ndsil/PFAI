/* -*- Mode:Prolog; coding:iso-8859-1; indent-tabs-mode:nil; prolog-indent-width:8; prolog-paren-indent:4; tab-width:8; -*- 
Constraint store

Author: Tony Lindgren

*/
:- use_module([library(clpfd)]).

zebra:-
        % Define variabels and their domain      
        House_colors = [Red, Green, White, Yellow, Blue],
        domain(House_colors, 1, 5), 

        %TODO 
        Nationalities = [English, Swede, Dane, Norwegian, German], 
        domain(Nationalities, 1, 5),

        Pets = [Dog, Cats, Birds, Horse, Zebra],
        domain(Pets, 1, 5),

        Smokes = [PallMall, DunHill, BlueMaster, Prince, Blend],
        domain(Smokes, 1, 5),

        Drinks = [Tea, Coffee, Water, Milk, Beer],
        domain(Drinks, 1, 5),     
        
       %TODO - add more constraints and relations       
        % Define constraints and relations
        all_different(House_colors),       
        all_different(Nationalities),      
        all_different(Smokes),
        all_different(Drinks),
        all_different(Pets),
        Red #= English,
        Swede #= Dog,
        Dane #= Tea,
        Green #= White - 1,
        Green #= Coffee,
        PallMall #= Birds,
        Yellow #= DunHill,
        Milk #= 3, 
        Norwegian #= 1,
        BlueMaster #= Beer,
        German #= Prince,
        (Cats #= Blend + 1) #\/ (Cats #= Blend - 1),
        (Yellow #= Horse + 1) #\/ (Yellow #= Horse - 1),            
        (Blue #= Norwegian + 1) #\/ (Blue #= Norwegian - 1),
        (Water #= Blend + 1) #\/ (Water #= Blend - 1),

        %TODO - append all variabels
        % append variables to one list
        append(House_colors, Nationalities, Temp1),
        append(Temp1, Pets, Temp2),
        append(Temp2, Drinks, Temp3),
        append(Temp3, Smokes, VariableList),

        labeling([], VariableList), 

        % connect answers with right objects
        sort([Red-red, Green-green, White-white, Yellow-yellow, Blue-blue], House_color_connection),
        sort([English-english, Swede-swede, Dane-dane, Norwegian-norwegian, German-german], Nation_connection),
        sort([Dog-dog, Cats-cats, Birds-birds, Horse-horse, Zebra-zebra], Pet_connection),
        sort([PallMall-pallmall, DunHill-dunhill, BlueMaster-bluemaster, Prince-prince, Blend-blend], Smokes_connection),
        sort([Tea-tea, Coffee-coffee, Water-water, Milk-milk, Beer-beer], Drinks_connection),

        %TODO - add sorting of all variabels
        % print solution
        Format = '~w~15|~w~30|~w~45|~w~60|~w~n',
        format(Format, ['house 1', 'house 2', 'house 3', 'house 4', 'house 5']),        
        format(Format, House_color_connection),                                                       
        format(Format, Nation_connection),
        format(Format, Pet_connection),
        format(Format, Smokes_connection),
        format(Format, Drinks_connection).