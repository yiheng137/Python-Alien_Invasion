import bullet


def get_move_range(obj_rect, screen_rect):
    """Compute the movement boundary of the object on the screen.
    Returns a tuple including (min_x, max_x, min_y, max_y)"""

    return (obj_rect.width // 2,  # minimum x
     screen_rect.width - obj_rect.width // 2,  # maximum x
     obj_rect.height // 2,  # minimum y,
     screen_rect.height - obj_rect.height // 2)  # restrict the motion position of the ship on the screen


def fire_bullet(ai_settings, screen, ship, bullet_lst):
    """Create a new bullet and add it to the bullets group."""
    # Limit the number of bullet on the screen
    if len(bullet_lst) < ai_settings.bullet_allowed:
        new_bullet = bullet.Bullet(ai_settings, screen, ship)
        bullet_lst.add(new_bullet)
