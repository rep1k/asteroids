import pygame
import constants
import player as p


def print_start_message():
    print("Starting asteroids!")


def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    time_object = pygame.time.Clock()
    player = p.Player(
        x=(constants.SCREEN_WIDTH / 2),
        y=(constants.SCREEN_HEIGHT / 2),
    )
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        player.draw(screen)
        dt = time_object.tick(60) / 1000


if __name__ == "__main__":
    main()
