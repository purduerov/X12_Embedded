/*
 * led.c
 *
 *  Created on: Nov 14, 2020
 *      Author: Conne
 */

#include "led.h"

TIM_HandleTypeDef timerConfiguration;

#define ARR_1HZ (800 - 1)
#define ARR_2HZ (400 - 1)
#define ARR_4HZ (200 - 1)
#define ARR_8HZ (100 - 1)
#define ARR_16HZ (50 - 1)
#define ARR_32HZ (25 - 1)

void InitializeTimer(TIM_TypeDef* timerModule)
{
	timerConfiguration.Instance = timerModule;
	//  CK_CNT Frequency is 1.6kHz
	//  Assuming Internal 8MHz is CLK source (CK_PSC)
	timerConfiguration.Init.Prescaler = 5000 - 1;
	timerConfiguration.Init.CounterMode = TIM_COUNTERMODE_UP;
	timerConfiguration.Init.Period = ARR_1HZ;
	timerConfiguration.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_ENABLE;
	timerConfiguration.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
	timerConfiguration.State = HAL_TIM_STATE_RESET;

	HAL_TIM_Base_Init(&timerConfiguration);
}

//  With Auto Reload Preload Enabled, new Frequency is not set until next Update Event
//  which is when counter overflows
void flashLed(TimerFrequency timerFrequency)
{
	uint32_t newArr;

	switch (timerFrequency)
	{
		case TIM_FREQ_1HZ: newArr = ARR_1HZ; break;
		case TIM_FREQ_2HZ: newArr = ARR_2HZ; break;
		case TIM_FREQ_4HZ: newArr = ARR_4HZ; break;
		case TIM_FREQ_8HZ: newArr = ARR_8HZ; break;
		case TIM_FREQ_16HZ: newArr = ARR_16HZ; break;
		case TIM_FREQ_32HZ: newArr = ARR_32HZ; break;
		default: newArr = ARR_1HZ;
	}

	timerConfiguration.Instance->ARR = newArr;
}
