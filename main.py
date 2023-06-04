from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstWindow(Screen):
    pass
class Constitution(Screen):
    pass
class ConstitutionR1(Screen):
    pass
class ConstitutionR1G1(Screen):
    pass
class ConstitutionR1G2(Screen):
    pass
class ConstitutionR1G3(Screen):
    pass
class ConstitutionR1G4(Screen):
    pass
class ConstitutionR1G5(Screen):
    pass
class ConstitutionR1G6(Screen):
    pass
class ConstitutionR1G7(Screen):
    pass
class ConstitutionR1G8(Screen):
    pass
class ConstitutionR1G9(Screen):
    pass
class ConstitutionR2(Screen):
    pass
class CC(Screen):
    pass
class CCFirstPart(Screen):
    pass
class CCFirstPartR1(Screen):
    pass
class CCFirstPartR1G1(Screen):
    pass
class CCFirstPartR1G2(Screen):
    pass
class CCFirstPartR2(Screen):
    pass
class CCFirstPartR2G3(Screen):
    pass
class CCFirstPartR2G4(Screen):
    pass
class CCFirstPartR2G5(Screen):
    pass
class CCFirstPartR2G6(Screen):
    pass
class CCFirstPartR2G7(Screen):
    pass
class CCFirstPartR2G8(Screen):
    pass
class CCFirstPartR3(Screen):
    pass
class CCFirstPartR3G9(Screen):
    pass
class CCFirstPartR3G9Part1(Screen):
    pass
class CCFirstPartR3G9Part2(Screen):
    pass
class CCFirstPartR3G10(Screen):
    pass
class CCFirstPartR3G10Part1(Screen):
    pass
class CCFirstPartR3G10Part2(Screen):
    pass
class CCFirstPartR4(Screen):
    pass
class CCFirstPartR4G11(Screen):
    pass
class CCFirstPartR4G12(Screen):
    pass
class CCFirstPartR4G13(Screen):
    pass
class CCFirstPartR5(Screen):
    pass
class CCFirstPartR5G14(Screen):
    pass
class CCFirstPartR6(Screen):
    pass
class CCFirstPartR6G15(Screen):
    pass
class CCSecondPart(Screen):
    pass
class CCSecondPartR7(Screen):
    pass
class CCSecondPartR7G16(Screen):
    pass
class CCSecondPartR7G16Part1(Screen):
    pass
class CCSecondPartR7G16Part2(Screen):
    pass
class CCSecondPartR7G17(Screen):
    pass
class CCSecondPartR7G18(Screen):
    pass
class CCSecondPartR7G19(Screen):
    pass
class CCSecondPartR7G19Part1(Screen):
    pass
class CCSecondPartR7G19Part2(Screen):
    pass
class CCSecondPartR7G19Part3(Screen):
    pass
class CCSecondPartR7G20(Screen):
    pass
class CCSecondPartR8(Screen):
    pass
class CCSecondPartR8G21(Screen):
    pass
class CCSecondPartR8G21Part1(Screen):
    pass
class CCSecondPartR8G21Part2(Screen):
    pass
class CCSecondPartR8G21Part3(Screen):
    pass
class CCSecondPartR8G22(Screen):
    pass
class CCSecondPartR8G22Part1(Screen):
    pass
class CCSecondPartR8G22Part2(Screen):
    pass
class CCSecondPartR8G22Part3(Screen):
    pass
class CCSecondPartR8G22Part4(Screen):
    pass
class CCSecondPartR8G22Part5(Screen):
    pass
class CCSecondPartR8G22Part6(Screen):
    pass
class CCSecondPartR8G22Part7(Screen):
    pass
class CCSecondPartR8G22Part8(Screen):
    pass
class CCSecondPartR8G22Part9(Screen):
    pass
class CCSecondPartR8G23(Screen):
    pass
class CCSecondPartR9(Screen):
    pass
class CCSecondPartR9G24(Screen):
    pass
class CCSecondPartR9G24Part1(Screen):
    pass
class CCSecondPartR9G24Part2(Screen):
    pass
class CCSecondPartR9G24Part3(Screen):
    pass
class CCSecondPartR9G24Part4(Screen):
    pass
class CCSecondPartR9G24Part5(Screen):
    pass
class CCSecondPartR9G25(Screen):
    pass
class CCSecondPartR9G25Part1(Screen):
    pass
class CCSecondPartR9G25Part2(Screen):
    pass
class CCSecondPartR9G25Part3(Screen):
    pass
class CCSecondPartR9G25Part4(Screen):
    pass
class CCSecondPartR9G26(Screen):
    pass
class CCSecondPartR9G26Part1(Screen):
    pass
class CCSecondPartR9G26Part2(Screen):
    pass
class CCSecondPartR9G27(Screen):
    pass
class CCSecondPartR9G27Part1(Screen):
    pass
class CCSecondPartR9G27Part2(Screen):
    pass
class CCSecondPartR9G28(Screen):
    pass
class CCSecondPartR10(Screen):
    pass
class CCSecondPartR10G29(Screen):
    pass
class CCSecondPartR10G29Part1(Screen):
    pass
class CCSecondPartR10G29Part2(Screen):
    pass
class CCSecondPartR10G30(Screen):
    pass
class CCSecondPartR10G30Part1(Screen):
    pass
class CCSecondPartR10G30Part2(Screen):
    pass
class CCSecondPartR10G30Part3(Screen):
    pass
class CCSecondPartR10G31(Screen):
    pass
class CCSecondPartR10G31Part1(Screen):
    pass
class CCSecondPartR10G31Part2(Screen):
    pass
class CCSecondPartR10G32(Screen):
    pass
class CCSecondPartR10G32Part1(Screen):
    pass
class CCSecondPartR10G32Part2(Screen):
    pass
class CCSecondPartR11(Screen):
    pass
class CCSecondPartR11G33(Screen):
    pass
class CCSecondPartR11G33Part1(Screen):
    pass
class CCSecondPartR11G33Part2(Screen):
    pass
class CCSecondPartR12(Screen):
    pass
class CCSecondPartR12G34(Screen):
    pass


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('myKv.kv')

class LegRefRFApp(App):
    def build(self):
        return kv


if __name__=='__main__':
    LegRefRFApp().run()