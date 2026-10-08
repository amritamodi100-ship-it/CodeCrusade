'''The Bouncer's Bug: We want a bouncer program that grants access IF a patron meets
one of two criteria: they are strictly over 18 AND hold a VIP pass, 
OR they are over 21 regardless of VIP status. The code below is logically flawed 
and will let unauthorized people inside. Rewrite the Boolean expression using parentheses
so the precedence strictly enforces our exact architectural rules.'''

age = 19
is_vip = True

can_enter =(age > 18 and is_vip)  or ( age > 21 )
print(can_enter)


