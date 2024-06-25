package Prova.Prova_09_08.java;

import javax.jms.*;
import java.util.Hashtable;
import javax.naming.*;


public class Extractor {

    public static void main(String[] args) {
        
        Hashtable<String, String> prop = new Hashtable<String, String>();
        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");

        prop.put("topic.data", "mydata");
        prop.put("topic.temp", "mytemp");
        prop.put("topic.press", "mypress");

        try {

            Context jndiContext = new InitialContext(prop);
            TopicConnectionFactory connectionFactory = (TopicConnectionFactory) jndiContext.lookup("TopicConnectionFactory");
            Topic topic = (Topic) jndiContext.lookup("data");
            Topic topic_temp = (Topic) jndiContext.lookup("temp");
            Topic topic_press = (Topic) jndiContext.lookup("press");

            TopicConnection topicConnection = connectionFactory.createTopicConnection();
            topicConnection.start();
            TopicSession topicSession = topicConnection.createTopicSession(false, 0);
            TopicSubscriber topicSubscriber = topicSession.createSubscriber(topic);

            MsgListener listener = new MsgListener(topic_press, topic_temp, topicSession);
            topicSubscriber.setMessageListener(listener);

            while (true) {
                Thread.sleep(2000);
            }




        } catch (NamingException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (JMSException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
    
}
