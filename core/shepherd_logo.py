#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports.
import sys # System.
import time # The time.
import os # Operating System functions.
import subprocess # So we can call other scripts!
import re # Regular expression, because we all love that... right?
import argparse # Google said I needed this.
import core.colors as colors # We all love a splash of color.
import core.mods as mods # So we can let people modify it easier!

# Main logo.
def shepherd_logo():
  mods.clear_screen()
  print(colors.bcolors.BLINK + '''
                                  &&##########&&                                                                           
                          #PY?7!~^^:::::::::::^^^~!7?Y5G#&                                                                 
                     #PY5P55Y7^. .......................:^7G  ##                                                           
                 &G?~.. ..:^75BBY^..........................~G#J~7YG&                                                      
               G?^. ..........:!P&P~..........................J P. .:!YB                                                   
             P~. ................~B ?.::::::::::::::::.........J G.... .^?P&                                               
           P~.............:::::....P J...............::::.......G ?...... .:?G                                             
         B!...........:::.....:^~!7?  55PPPP55YJ?7!^::......:...? G......... .^JB                                          
        Y. ........::....^!J5G###BBGG& BYYYY5PPGB##&#BG5?!^.....7 G............ .7P                                        
       7 ........:...:!YB& #PJ7~^:...^J#5:.......::^!7YPB#&B57^.5 ?................~P                                      
      ! ..........:!5&  G?~:...........~&B:..............:~?P&&G P...::..............~P                                    
     7 .........:JB  B?^................7 J...............:JG&   &BJ~...:::............7&                                  
    5 .........?#  #7.................. .#B  ............:G BG&      G7:..::::......... ? #&                               
   &: .......^G   5:..............^~7JJYY&BJJJ?!~^:......:# J.^?5#     #5~..:::.........:#&!5                              
   #?J?7~:..^B   Y.......... .^?PB&              &#G5?~:. Y P....:~?5B&   G7:............G ? ~G                            
   J~!7?5PY~P   B:.........^JG                         &GJ!##:........^7YB  B7...........G P...!B                          
  #:.....:!P    ? ...... ^5&                               # ?............^?G B!.........B P... .?#                        
  P....... J    YJYYJ7^:Y                             &GY7~~&#:......::.... .~Y&G^......~  Y..... :5                       
  5 .......G    G7!!7J5#                           &P7^.....P Y.....:G#BG5?~:  ^P&?.....P  ~....... ~B                     
  J ......:#    Y ..  7                          #J^........^& ?.....Y      #5!. ? P:..!  P......... .5                    
  5 ......^&    G.... J                        &J: ......:::.~# ?....:G        B?.7 B^:# G:............P                   
  P.......~     &^... ?                       5: .......:::::.^P P^...:P         #?G BG  P?!^......... 7                   
  #:......^&     5 .. ^                     #7.........:::::::..!G#5~...!P         &   #Y   &BY~.......G                   
   ! .....:#      ! .. 5                   G^ .......:::::::::::..~5BGJ~:.^?P#&      BJ^.?#     7......7&                  
   P ......G      &~ . :#                 P.......:::::::::::::::..:J&  #P5JJJ5B&BPJ~:..:.^?P&  G.......^P                 
    ~ .... ?       &! . ^&               5..........::::::::::::.:Y&  BJ~^7??7!~^:...::::::..^7PG::::.....7#               
    G......:#        J.  ^#             P  .:^~!7!~~^:...::::::.!#  B!:...........::::::::::::..^:::::.....:5              
     J .... 7         B!  .P           G^7YPPP55Y55PPP5?!:..::.!&  J:.::::::::::::::::::::::::::::::::::.....!B            
      7 .....P          G7. !B         BPP ~........:^!?5PY!:.^&  ?.:::::::::::::::::::::::::::::::::::::.....:J&          
       ! .....B           #5!^?B      #?.~ ?..::::::::...:!YP7Y  G.::::::::::::::::::::::::::::::::::::::::.....^G         
        ?  .. :B             &GPG&   P: .^ B:.::::::::::::..^J   5.::::::.....::::::::::::::::::::::::::::::......?&       
         5. .. :G                   5.....P 5..:::::::::::::.~   #^.::::.......:::::::::::::::::::::::::::::...... ^G      
          B!  . .Y                 G......~  Y..::::::::::::::G   B^..:..^JY?~:..::::::..::::..:::::::::::::....:?J^ 7     
            P^    !#              &^.......7  G~..:::::::::::.^B   &?....B    BJ^..::.:?GGPP5Y?~:.:::::::::.....^#  ! P    
             &5^   :Y             5 ........!#  5~..::::::::::.:Y&   G!..G      &5~..^BG!^::^!J#BJ^..::::::.......?&#7#    
                P!.  ^P           7 ......::.:JB  G?^...:::::::..~5&   BJ?#        P~5 P7:.....^5  5~..::......... J       
                  #J^  ~P         !.......::::.:~JP##GY!^:...:::...^J#   &&          BJ~JGY~..:..~5  G!........... P       
                     BY~.^5&      7 .......::::::..:~?5B#B5?~:.......:?B           B?:...:JBP!.....^Y# B?:....  .:?        
                        &PJ?5#    P ........:::::::::..:^75#&#57:.......7B       &J:.......:Y&P^......!YBBJ^~!JPB&         
                            &#&    7 ........::::::::::::..:~JG&&P7:.....:Y     #~ ........ .!#&~.....  ^G                 
                                    ?...........::::::::::::...^?B #Y^.....?    ~ ........^YB&  P   .^7P&                  
                                     G!. ..........::::::::::::...~5& 5^....?  &:........!&     Y~?5B&                     
                                       BJ~................:::::::...:J& Y:...G  5........B                                 
                                          B5?~^.......................:Y #!..!   P^ .....Y                                 
                                              &BPY?!^:..................~B J.:#   &J: ....?&                               
                                                     #BP5?!~:.............5 Y.G     &Y^  . ^P                              
                                                            &B5?~:. .......J JG        P!.   !#                            
                                                                 #P?^. .... ? &          #?.  .Y                           
                                                                    &G?:  .. ?             #!   Y                          
                                                                       &5~    5              ?  ?                          
                                                                          G!. .B              ::#                          
                                                                            B! ~              JB                           
                                                                              G^5                                          
                                                                               &P
                                       _____ _                    _                        _
                                      (      /        ___  \,___, /        ___  .___    ___/
                                       `--.  |,---. .'   ` |    \ |,---. .'   ` /   \  /   |
                                          |  |'   ` |----' |    | |'   ` |----' |   ' ,'   |
                                     \___.'  /    | `.___, |`---' /    | `.___, /     `___,'
                                                           \                               `
  ''' + colors.bcolors.ENDC)
  
  for i in range(100+1): # Makes it load to exactly 100% without stunting or stopping for no reason.
    time.sleep(0.05) # Change load times by changing this!
    sys.stdout.write(('='*i)+(''*(100-i))+(" \r [%d"%i+"%] ")) # Fancy math to make the loading bar.
    sys.stdout.flush() # Yes, this function thing.

  mods.clear_screen() # Runs the clear screen mod.
  print(f'''
#                                 {colors.bcolors.RED}(♥{colors.bcolors.ENDC} v 2.2.3 {colors.bcolors.RED}♥){colors.bcolors.ENDC}
#
#  Lead & Developer:                 {colors.bcolors.RED}Shepherd{colors.bcolors.ENDC}
#  Main repository : {colors.bcolors.UNDERLINE}https://github.com/LostShepherdUK/Shepherd-Project{colors.bcolors.ENDC}
#  
#  {colors.bcolors.BOLD}NOTICE:{colors.bcolors.ENDC} {colors.bcolors.BLINK}Onus is on the user for using within the remits of the law.{colors.bcolors.ENDC}
#  (The developers nor open source framework developers are responsible for any actions performed by the end user){colors.bcolors.ENDC}
''')