import pygame


def get_user_input():
    """Collect user input for visualization parameters using Pygame"""
    pygame.init()
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption('Sorting Visualization Setup')
    
    # Colors
    BACKGROUND_COLOR = (245, 245, 245)
    INPUT_COLOR = (255, 255, 255)
    BORDER_COLOR = (100, 100, 100)
    BUTTON_COLOR = (0, 123, 255)
    BUTTON_HOVER_COLOR = (30, 144, 255)
    DROPDOWN_COLOR = (220, 220, 220)
    TEXT_COLOR = (30, 30, 30)
    HEADER_COLOR = (0, 123, 255)

    # Fonts
    pygame.font.init()
    font = pygame.font.Font(pygame.font.match_font('arial'), 28)
    small_font = pygame.font.Font(pygame.font.match_font('arial'), 20)
    header_font = pygame.font.Font(pygame.font.match_font('arial'), 36)

    # Input fields
    num_elements_input = ''
    update_interval_input = ''
    algorithm_options = ['Selection Sort','Insertion Sort', 'Merge Sort','Heap Sort', 'Quick Sort']
    selected_algorithm = algorithm_options[0]

    # Rectangles for input fields and buttons
    num_elements_rect = pygame.Rect(150, 140, 200, 40)
    update_interval_rect = pygame.Rect(150, 210, 200, 40)
    algorithm_rect = pygame.Rect(150, 280, 200, 40)
    start_button_rect = pygame.Rect(150, 500, 200, 50)

    dropdown_active = False
    active_input = None

    running = True

    while running:
        screen.fill(BACKGROUND_COLOR)

        # Header
        header_text = header_font.render('Sorting Visualizer Setup', True, HEADER_COLOR)
        screen.blit(header_text, (60, 50))

        # Number of elements input
        pygame.draw.rect(screen, INPUT_COLOR, num_elements_rect)
        pygame.draw.rect(screen, BORDER_COLOR, num_elements_rect, 2)
        num_elements_label = small_font.render('Number of Elements:', True, TEXT_COLOR)
        num_elements_text = font.render(num_elements_input or '50', True, TEXT_COLOR)
        screen.blit(num_elements_label, (num_elements_rect.x, num_elements_rect.y - 30))
        screen.blit(num_elements_text, (num_elements_rect.x + 10, num_elements_rect.y + 5))

        # Update interval input
        pygame.draw.rect(screen, INPUT_COLOR, update_interval_rect)
        pygame.draw.rect(screen, BORDER_COLOR, update_interval_rect, 2)
        update_interval_label = small_font.render('Update Interval (sec):', True, TEXT_COLOR)
        update_interval_text = font.render(update_interval_input or '0.5', True, TEXT_COLOR)
        screen.blit(update_interval_label, (update_interval_rect.x, update_interval_rect.y - 30))
        screen.blit(update_interval_text, (update_interval_rect.x + 10, update_interval_rect.y + 5))

        # Algorithm selection
        pygame.draw.rect(screen, INPUT_COLOR, algorithm_rect)
        pygame.draw.rect(screen, BORDER_COLOR, algorithm_rect, 2)
        algorithm_label = small_font.render('Select Algorithm:', True, TEXT_COLOR)
        algo_text = font.render(selected_algorithm, True, TEXT_COLOR)
        screen.blit(algorithm_label, (algorithm_rect.x, algorithm_rect.y - 30))
        screen.blit(algo_text, (algorithm_rect.x + 10, algorithm_rect.y + 5))

        # Dropdown options if active
        if dropdown_active:
            for i, option in enumerate(algorithm_options):
                option_rect = pygame.Rect(150, 320 + i * 40, 200, 40)
                pygame.draw.rect(screen, DROPDOWN_COLOR, option_rect)
                pygame.draw.rect(screen, BORDER_COLOR, option_rect, 1)
                option_text = font.render(option, True, TEXT_COLOR)
                screen.blit(option_text, (option_rect.x + 10, option_rect.y + 5))

        # Start button
        button_color = BUTTON_COLOR
        if start_button_rect.collidepoint(pygame.mouse.get_pos()):
            button_color = BUTTON_HOVER_COLOR
        pygame.draw.rect(screen, button_color, start_button_rect)
        start_text = font.render('Start', True, (255, 255, 255))
        screen.blit(start_text, (start_button_rect.x + 70, start_button_rect.y + 10))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check input fields
                if num_elements_rect.collidepoint(event.pos):
                    active_input = 'num_elements'
                elif update_interval_rect.collidepoint(event.pos):
                    active_input = 'update_interval'
                elif algorithm_rect.collidepoint(event.pos):
                    dropdown_active = not dropdown_active
                elif dropdown_active:
                    for i, option in enumerate(algorithm_options):
                        option_rect = pygame.Rect(150, 320 + i * 40, 200, 40)
                        if option_rect.collidepoint(event.pos):
                            selected_algorithm = option
                            dropdown_active = False
                elif start_button_rect.collidepoint(event.pos):
                    return {
                        'num_elements': int(num_elements_input or '50'),
                        'update_interval': float(update_interval_input or '0.5'),
                        'algorithm': selected_algorithm
                    }

            if event.type == pygame.KEYDOWN:
                if active_input == 'num_elements':
                    if event.key == pygame.K_BACKSPACE:
                        num_elements_input = num_elements_input[:-1]
                    elif event.unicode.isdigit():
                        num_elements_input += event.unicode
                elif active_input == 'update_interval':
                    if event.key == pygame.K_BACKSPACE:
                        update_interval_input = update_interval_input[:-1]
                    elif event.unicode.isdigit() or event.unicode == '.':
                        update_interval_input += event.unicode

        pygame.display.flip()