import pygame

from settings import WINDOW_SIZE, BACKGROUND_COLOR, FRAME_RATE, UPDATE_INTERVAL, FONT_SIZE, TEXT_COLOR

from snake import Snake
from apple import Apple

# Initialize pygame and the screen and make a clock, so we can control the framerate
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")

update_event_id = pygame.USEREVENT + 1
pygame.time.set_timer(update_event_id, UPDATE_INTERVAL)

# This is our great snake that will be doing all the work
snake = Snake()

# Our apple will never actually change. It will always be the same object
# but once they hit it, it will just register that it hit and move locations
apple = pygame.sprite.GroupSingle(Apple())
apple.sprites()[0].place()

# Get the high score
try:
    high_score_file = open("high_score.txt", "r")
    high_score = int(high_score_file.read())
    high_score_file.close()
except FileNotFoundError:
    high_score = 0


is_high_score = False

# If the screen should be up or not
running = True

# If we are playing or not (this will be false once the score is displayed)
playing = True

# Main game loop
while running:
    # Check if the user wants to quit
    for event in pygame.event.get():
        # Pressing the close button the window shuts it down
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Pressing escape shuts it down too
            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                snake.up()

            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                snake.right()

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                snake.down()

            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                snake.left()

            elif event.key == pygame.K_RETURN and not playing:
                snake = Snake()
                apple = pygame.sprite.GroupSingle(Apple())
                apple.sprites()[0].place()

                playing = True

        elif event.type == update_event_id:

            # If we are still playing, update things
            if playing:

                # Update the apple and then the snake (the apple may be under the snake)
                apple.update()
                snake.update()

    # If the snake has hit the apple, add a new body part and place the apple elsewhere
    if snake.body[0].rect.colliderect(apple.sprites()[0].rect):
        snake.add_new_body_part()
        apple.sprites()[0].place()

    # If the snake is dead then we are done
    if snake.is_dead():
        playing = False


    # Fill the background
    screen.fill(BACKGROUND_COLOR)
    # Draw apple
    apple.draw(screen)
    # Draw snake
    snake.draw(screen)

    # And if we are not playing we need to display a score
    if not playing:
        font = pygame.font.SysFont("feesanbolt.ttf", FONT_SIZE)

        # If we have beaten the high score, display a happy message!
        if snake.length() >= high_score:
            high_score = snake.length()

            high_score_text = font.render("New High Score!", True, TEXT_COLOR)
            high_score_text_rect = high_score_text.get_rect()
            high_score_text_rect.center = (WINDOW_SIZE.width // 2, WINDOW_SIZE.height // 4)

            screen.blit(high_score_text, high_score_text_rect)

        # Display the score
        score_text = font.render(str(snake.length()), True, TEXT_COLOR)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (WINDOW_SIZE.width // 2, WINDOW_SIZE.height // 2)

        screen.blit(score_text, score_text_rect)


        # Display restart instructions

        restart_text = font.render("Press Enter to Restart", True, TEXT_COLOR)
        restart_text_rect = restart_text.get_rect()
        restart_text_rect.center = (WINDOW_SIZE.width // 2, WINDOW_SIZE.height * 3 // 4)

        screen.blit(restart_text, restart_text_rect)


    # Update screen
    pygame.display.flip()

    # We want a slow framerate so we can get the slow and discrete snake moving in jumps
    clock.tick(FRAME_RATE)

# Update high_score (if snake.length < high_score, the file won't change)

high_score_file = open("high_score.txt", "w")
high_score_file.write(str(high_score))
high_score_file.close()
pygame.quit()
