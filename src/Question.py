from Scene import Scene
from Victory import Victory
from DatabaseHandler import DatabaseHandler
from Human import Human
from Computer import Computer
import random
import pygame
import logging
class Question(Scene):
    def __init__(self, color, previous, player, final, give_pie=False):
        super().__init__()
        self.logger = logging.getLogger("Question")
        logging.basicConfig(format='%(asctime)s - %(name)s: %(levelname)s - %(message)s', level=logging.INFO)
        self.final = final
        self.color = color
        self.previous = previous
        self.player = player
        self.handler = DatabaseHandler()
        if color == 'black':
            self.color = random.choice(['green', 'white', 'red', 'blue'])
        self.question = self.handler.select_color_question(self.color)
        self.answers = []
        self.answers.append(self.question['correct'])
        self.answers += self.question['incorrect']
        random.shuffle(self.answers)
        self.font = pygame.font.SysFont("Arial", 14) 
        self.selected_answer = ""
        self.width, self.height = pygame.display.get_surface().get_size()
        self.delay = 0
        self.give_pie = give_pie
        self.logger.info("Asking {0} a {1} question".format(self.player.name, self.color))
    def process_input(self, events):
        if type(self.player) is Human:    
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.switch_scene(self.previous)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.selected_answer = self.answers[0]
                    if event.key == pygame.K_2:
                        self.selected_answer = self.answers[1]
                    if event.key == pygame.K_3:
                        self.selected_answer = self.answers[2]
                    if event.key == pygame.K_4:
                        self.selected_answer = self.answers[3]
        else:
            self.selected_answer = self.player.answer_question(self.question, self.answers)
        if self.selected_answer != '':
            self.logger.info("{0} answered {1} which is correct".format(self.player.name, self.selected_answer) if self.selected_answer == self.question['correct'] else "{0} answered {1} which is incorrect".format(self.player.name, self.selected_answer))
            if self.final:
                if self.selected_answer == self.question['correct']:
                    self.switch_scene(Victory(self.player))
                else:
                    self.previous.switch_player()
            else:
                if self.selected_answer == self.question['correct']:
                    if self.give_pie:
                        self.player.add_pie(self.color)
                else:
                    self.previous.switch_player()
                self.previous.next = self.previous
                self.switch_scene(self.previous)
    def update(self):
        pass
    def render(self, screen):
        caption = "Question for " + self.player.name 
        pygame.display.set_caption(caption)
        screen.fill(pygame.Color('black'))
        question = self.font.render(self.question['question'], True, pygame.Color(self.color))
        self.player.draw_statistics(screen, self.width/2 - 150, 10)
        question_rect = question.get_rect(center=(self.width/2, self.height/3))
        screen.blit(question, question_rect)
        offset = 50
        if self.selected_answer == self.question['correct']:
            color = 'green'
        else:
            color = 'red'
        for i in range(len(self.answers)):
            answer = self.font.render(str(i + 1) + ": " + self.answers[i], True, pygame.Color(self.color))
            answer_rect = answer.get_rect(center=(self.width/2, self.height/3 + offset))
            if self.answers[i] == self.selected_answer:
                pygame.draw.rect(screen, pygame.Color(color), answer_rect, 2)
            screen.blit(answer, answer_rect)
            offset += 50
        pygame.time.wait(1000)


        