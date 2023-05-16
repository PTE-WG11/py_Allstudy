import pygame
import random

# 初始化pygame
pygame.init()

# 定义窗口尺寸
width, height = 800, 600

# 创建窗口
screen = pygame.display.set_mode((width, height))

# 设置标题
pygame.display.set_caption("我的游戏")

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 定义字体
font = pygame.font.SysFont(None, 30)


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 5
        if self.rect.y > height:
            self.rect.y = random.randrange(-100, -10)
            self.rect.x = random.randrange(0, width)


# 创建精灵组
all_sprites_list = pygame.sprite.Group()

# 创建方块精灵
block_list = pygame.sprite.Group()

for i in range(50):
    block = Block(black, 20, 20)
    block.rect.x = random.randrange(width)
    block.rect.y = random.randrange(height)
    block_list.add(block)
    all_sprites_list.add(block)

# 定义游戏结束函数
def gameover():
    gameover_font = pygame.font.SysFont(None, 60)
    gameover_text = gameover_font.render("Game Over", True, red)
    screen.blit(gameover_text, [200, 250])
    pygame.display.flip()
    pygame.time.wait(2000)

# 初始化变量
score = 0
player_speed = 5

# 创建玩家精灵
player = pygame.sprite.Sprite()
player.image = pygame.Surface([50, 50])
player.image.fill(white)
player.rect = player.image.get_rect()
player.rect.x = int(width/2)
player.rect.y = int(height/2)
all_sprites_list.add(player)

# 游戏循环
running = True
while running:
    # 检测事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.rect.y -= player_speed
            elif event.key == pygame.K_DOWN:
                player.rect.y += player_speed
            elif event.key == pygame.K_LEFT:
                player.rect.x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player.rect.x += player_speed

    # 清空屏幕
    screen.fill(white)

    # 更新所有精灵
    all_sprites_list.update()

    # 检测碰撞
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
    for block in blocks_hit_list:
        score += 1
        print("得分：", score)

    # 绘制所有精灵
    all_sprites_list.draw(screen)

    # 绘制得分
    score_text = font.render("得分：" + str(score), True, black)
    screen.blit(score_text, [10, 10])

    # 判断游戏结束条件
    if player.rect.x < 0 or player.rect.x > width or player.rect.y < 0 or player.rect.y > height:
        gameover()
        running = False

    # 刷新屏幕
    pygame.display.flip()

# 退出pygame
pygame.quit()
