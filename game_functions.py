import sys
import pygame
import bullet
import alien


def fire_bullet(ai_settings, screen, ship, bullet_lst):
    """Create a new bullet and add it to the bullets group."""
    # Limit the number of bullet on the screen
    if len(bullet_lst) < ai_settings.bullet_allowed:
        new_bullet = bullet.Bullet(ai_settings, screen, ship)
        bullet_lst.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    new_alien = alien.Alien(ai_settings, screen)
    alien_width = new_alien.rect.width
    available_space_x = screen.get_width() - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    # Create the first row of aliens.
    for num in range(number_aliens_x):
        # Create an alien and place it in the row.
        new_alien = alien.Alien(ai_settings, screen)
        new_alien.x = alien_width + 2 * alien_width * num
        new_alien.rect.x = new_alien.x
        aliens.add(new_alien)