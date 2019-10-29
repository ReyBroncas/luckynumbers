from sequences import *
from essential import *
from res import *
import time

x=2
diff_list = ((0,20),(21,100),(101,200))
revolver = denester(revolver,9,len(revolver)/9)
qustion_text_1 = denester(question_text_1,5,len(question_text_1)/5)
revolver_shot = denester(revolver_shot,9,len(revolver_shot)/9)
cowboy_alive = denester(cowboy_alive,16,len(cowboy_alive)/16)
cowboy_dead = denester(cowboy_dead,16,len(cowboy_dead)/16)
user_live = denester(user_live,9,len(user_live)/9)
heart = denester(heart,2,len(heart)/2)
text_area = qustion_area_maker(qustion_text_1)


start_logo = denester(start_logo,20,len(start_logo)/20)
landscape_1 = denester(landscape_1,20,len(landscape_1)/20)
blank_space_startup = denester(blank_space_startup,1,len(blank_space_startup)/1)

#! Animation
user_x_anim = [user_x_anim_1,user_x_anim_2,user_x_anim_3,user_x_anim_4,user_x_anim_5,user_x_anim_6,user_x_anim_7,user_x_anim_1,user_x_anim_1,user_x_anim_1]
man_x_anim = [man_x_anim_1,man_x_anim_1,man_x_anim_1,man_x_anim_1,man_x_anim_1,man_x_anim_1,man_x_anim_1,man_x_anim_8,man_x_anim_9,man_x_anim_1]
user_y_anim = [user_y_anim_1,user_y_anim_2,user_y_anim_3,user_y_anim_4,user_y_anim_5,user_y_anim_6,user_y_anim_7,user_y_anim_8,user_y_anim_9,user_y_anim_10]
man_y_anim = [man_y_anim_1,man_y_anim_1,man_y_anim_1,man_y_anim_1,man_y_anim_1,man_y_anim_1,man_y_anim_1,man_y_anim_1,man_y_anim_1,man_y_anim_1]

anim_x_global_line = []
anim_y_global_line = []
i=0
while i < len(user_x_anim):
    user_x_anim[i] = denester(user_x_anim[i],9,len(user_x_anim[i])/9)
    man_x_anim[i] = denester(man_x_anim[i],16,len(man_x_anim[i])/16)

    user_y_anim[i] = denester(user_y_anim[i],9,len(user_y_anim[i])/9)
    man_y_anim[i] = denester(man_y_anim[i],16,len(man_y_anim[i])/16)

    anim_x_global_line.append(draw_proccessing(text_area,user_x_anim[i],man_x_anim[i],0,0,0,0,[],True))
    anim_y_global_line.append(draw_proccessing(text_area,user_y_anim[i],man_y_anim[i],0,0,0,0,[],True))
    i+=1

#print(sequences.lucky_numbers(diff_list[x]))
#print(sequences.prime_numbers(diff_list[x]))
#print(sequences.ulam_numbers(diff_list[x]))


draw(blank_space_startup,start_logo,blank_space_startup)
time.sleep(2)
draw(blank_space_startup,landscape_1,blank_space_startup)
while 1:
    user_answer = input('\033[1;37;40m>>> ')
    if input_validator(user_answer)==True:
        if int(user_answer) == 2:
            exit()
        break
    else:
        continue













man_life_int = 5
user_life_int = 5

user_difficulty = choose_difficulty()



while man_life_int > 0 and user_life_int > 0:
    xyx = randomize_number_output(question_text_1, question_text_2, question_text_3)
    question_text = denester(xyx[0], 5, len(xyx[0]) / 5)
    question_text = qustion_area_maker(question_text)
    for i in range(0, 100):
        lucky_var, lucky_numbers1 = lucky_numbers(diff_list[user_difficulty - 1])
        prime_var, prime_numbers1 = prime_numbers(diff_list[user_difficulty - 1])
        ulam_var, ulam_numbers1 = ulam_numbers(diff_list[user_difficulty - 1])
        if (ulam_var == prime_var) or (prime_var == lucky_var) or (ulam_var == lucky_var) or \
                (lucky_var in prime_numbers1) or (lucky_var in ulam_numbers1) \
                or (prime_var in lucky_numbers1) or (prime_var in ulam_numbers1) \
                or (ulam_var in lucky_numbers1) or (ulam_var in prime_numbers1):
            continue
        else:
            break
    output_num_list = [lucky_var,prime_var,ulam_var]
    random.shuffle(output_num_list)
    line = draw_proccessing(question_text,user_live,cowboy_alive,heart,user_life_int,man_life_int,1,output_num_list)
    draw(line[0],line[1],line[2])

    #print(output_num_list[0],output_num_list[1],output_num_list[2])
    user_answer = input('\033[1;37;40m>>> ')
    if input_validator(user_answer)==True:
        user_answer = int(user_answer)
        if ((xyx[1]==1) and (user_answer==lucky_var)) or\
           ((xyx[1]==2) and (user_answer==prime_var)) or\
           ((xyx[1]==3) and (user_answer==ulam_var)):
            man_life_int -= 1
            line = draw_proccessing(question_text, user_live, cowboy_alive, heart, user_life_int, man_life_int, 1,output_num_list)
            animation_draw(anim_x_global_line,line[0],line[2])
            # draw(line[0], line[1])                                                                                       <---- ANIMATION
        else:
            user_life_int -= 1
            line = draw_proccessing(question_text, user_live, cowboy_alive, heart, user_life_int, man_life_int, 1,output_num_list)
            animation_draw(anim_y_global_line,line[0],line[2])
    else:
        continue

print("GAME OVER!")
