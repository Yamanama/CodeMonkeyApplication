from Scene import Scene
from Victory import Victory
from DatabaseHandler import DatabaseHandler
import random
import pygame
class Question(Scene):
    def __init__(self, color, previous, player, final):
        super().__init__()
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
        self.width, self.height = pygame.display.get_surface().get_size()
    def process_input(self, events):
        selected_answer = ""
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.switch_scene(self.previous)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_answer = self.answers[0]
                if event.key == pygame.K_2:
                    selected_answer = self.answers[1]
                if event.key == pygame.K_3:
                    selected_answer = self.answers[2]
                if event.key == pygame.K_4:
                    selected_answer = self.answers[3]
        if selected_answer != '':
            if self.final:
                print("FINAL ANSWER", selected_answer, self.question['correct'])
                if selected_answer == self.question['correct']:
                    self.switch_scene(Victory(self.player))
            else:
                if selected_answer == self.question['correct']:
                    self.player.add_pie(self.color)
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
        for i in range(len(self.answers)):
            answer = self.font.render(str(i + 1) + ": " + self.answers[i], True, pygame.Color(self.color))
            answer_rect = answer.get_rect(center=(self.width/2, self.height/3 + offset))
            screen.blit(answer, answer_rect)
            offset += 50



        