import pygame

screen = pygame.display.set_mode([700, 700])


def loza(nachalo_x, nachalo_y, dlina_stvola, shirina_vetki, tolshina, procent_dlini_potomka, procent_shirini_potomka,
         etazh=1, levo=None, pravo=None, etazh_otladki=0, derevo_otladki = 0, nomer_dereva=0, super_color=None, risuy_granici = False):
    print(nomer_dereva)
    if (levo is not None and nachalo_x < levo) or (pravo is not None and nachalo_x > pravo):
        return nachalo_x, nachalo_x, nachalo_y, nomer_dereva-1

    if dlina_stvola < 3 or shirina_vetki < 3 or (
            procent_shirini_potomka > 0.95 and procent_dlini_potomka > 0.95) or etazh > 900:
        return nachalo_x, nachalo_x, nachalo_y, nomer_dereva-1

    niz_stvola = [nachalo_x, nachalo_y]
    verh_stvola = [nachalo_x, nachalo_y - dlina_stvola]

    otladka_activna = derevo_otladki!=-1 and nomer_dereva==derevo_otladki
    if otladka_activna:
        color = [0, 255, 0]
    elif super_color is not None:
        color = super_color
    else:
        color = [100, 100, 100]
    pygame.draw.line(screen, color, niz_stvola, verh_stvola, tolshina)

    if (levo is None or verh_stvola[0] - shirina_vetki > levo) and (
            pravo is None or verh_stvola[0] - shirina_vetki < pravo):
        levo_est = True
        konec_levoy_vetki = [verh_stvola[0] - shirina_vetki, verh_stvola[1]]

        pygame.draw.line(screen, color, verh_stvola, konec_levoy_vetki, tolshina)
        nomer_dereva+=1
        if otladka_activna:
            super_color = [255, 50, 50]
        l_levo, l_pravo, l_verh, nomer_dereva = loza(konec_levoy_vetki[0], konec_levoy_vetki[1], dlina_stvola * procent_dlini_potomka,
                                       shirina_vetki * procent_shirini_potomka, tolshina, procent_dlini_potomka,
                                       procent_shirini_potomka, etazh=etazh + 1, levo=levo,
                                       pravo=nachalo_x, etazh_otladki = etazh_otladki, derevo_otladki=derevo_otladki, nomer_dereva=nomer_dereva, super_color=super_color, risuy_granici=otladka_activna)

        levo = l_pravo
        pravo = pravo
    else:
        levo_est = False
        l_verh = verh_stvola[1]

    if (pravo is None or verh_stvola[0] + shirina_vetki < pravo) and (
            levo is None or verh_stvola[0] + shirina_vetki > levo):
        pravo_est = True
        konec_pravoy_vetki = [verh_stvola[0] + shirina_vetki, verh_stvola[1]]
        pygame.draw.line(screen, color, verh_stvola, konec_pravoy_vetki, tolshina)
        nomer_dereva+=1
        if otladka_activna:
            super_color = [50, 255, 255]
        p_levo, p_pravo, p_verh, nomer_dereva = loza(konec_pravoy_vetki[0], konec_pravoy_vetki[1],
                                       dlina_stvola * procent_dlini_potomka, shirina_vetki * procent_shirini_potomka,
                                       tolshina, procent_dlini_potomka, procent_shirini_potomka, etazh=etazh + 1,
                                       levo=levo, pravo=pravo, etazh_otladki=etazh_otladki, derevo_otladki=derevo_otladki, nomer_dereva=nomer_dereva,super_color=super_color, risuy_granici=otladka_activna)
    else:
        pravo_est = False
        p_verh = verh_stvola[1]

    if levo_est:
        samaya_levaya_tochka = l_levo
    elif pravo_est:
        samaya_levaya_tochka = p_levo
    else:
        samaya_levaya_tochka = nachalo_x

    if pravo_est:
        samaya_pravaya_tochka = p_pravo
    elif levo_est:
        samaya_pravaya_tochka = l_pravo
    else:
        samaya_pravaya_tochka = nachalo_x

    if risuy_granici:
        pygame.draw.line(screen, [255, 0, 0], [samaya_levaya_tochka, nachalo_y], [samaya_levaya_tochka, verh_stvola[1]])
        pygame.draw.line(screen, [0, 0, 255], [samaya_pravaya_tochka, nachalo_y],
                         [samaya_pravaya_tochka, verh_stvola[1]])

    return samaya_levaya_tochka, samaya_pravaya_tochka, max(l_verh, p_verh), nomer_dereva


dlina_stvola = 200
shirina_vetki = 100
tolshina = 1
procent_dlini_potomka = 0.3
procent_shirini_potomka = 0.3

promotka_y = 0
etazh_otladki = 1
derevo_otladki = 0

pygame.key.set_repeat(10)
while True:
    events = pygame.event.get()
    change = -1 if pygame.KMOD_SHIFT & pygame.key.get_mods() else 1
    for e in events:
        if e.type == pygame.QUIT:
            exit()

        if e.type == pygame.KEYDOWN and e.key == pygame.K_1:
            dlina_stvola += change
        if e.type == pygame.KEYDOWN and e.key == pygame.K_2:
            shirina_vetki += change
        if e.type == pygame.KEYDOWN and e.key == pygame.K_3:
            procent_dlini_potomka += change / 100
        if e.type == pygame.KEYDOWN and e.key == pygame.K_4:
            procent_shirini_potomka += change / 100
        if e.type == pygame.KEYUP and e.key == pygame.K_5:
            etazh_otladki += change
        if e.type == pygame.KEYUP and e.key == pygame.K_6:
            derevo_otladki += change

        if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
            promotka_y = -verh
        if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
            promotka_y = 0

    screen.fill([0, 0, 0])
    res = loza(350, 700, dlina_stvola, shirina_vetki, tolshina, procent_dlini_potomka, procent_shirini_potomka,
               etazh_otladki=etazh_otladki, derevo_otladki=derevo_otladki)
    _, _, verh, _ = res
    if promotka_y > 0:
        screen.fill([0, 0, 0])
        loza(350, 700 + promotka_y + 50, dlina_stvola, shirina_vetki, tolshina, procent_dlini_potomka,
             procent_shirini_potomka, etazh_otladki=etazh_otladki, derevo_otladki = derevo_otladki)

    # print(res)
    pygame.display.flip()
